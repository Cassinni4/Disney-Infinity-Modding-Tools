/*
 * this script is literally held together by strings and duct tape
 * actionrouter is basically gateway with more steps (fuck me)
 * still wanna figure out that bottom chunk but I'll literally faint if I see that damn encryption again
 * by Cassinni4
 * original cool stuff by JiroTheOne
 * - corrects type-id (ASCII digit -> numeric)
 * - uses ASCII base IV "0123456789012345" and XORs positions 0,4,8,12 with table index
 * - trims control bytes and tries UTF-16LE fallback when appropriate
 */

const CryptoJS = require("crypto-js");
const fs = require("fs");

const logLevel = 0;
const sourceGatewayFile = "file.lua";
const decodedGatewayFile = "output.txt";

const key = CryptoJS.enc.Hex.parse("000102030405060708090a0b0c0d0e0f");
const baseIVstr = "0123456789012345";

var config = {
  iv: CryptoJS.enc.Hex.parse("00000000000000000000000000000000"),
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7
};

decryptGateway();

/* ----- main ----- */
function decryptGateway() {
  fs.readFile(sourceGatewayFile, null, (err, data) => {
    if (err) { console.error(err); return; }

    let fileStr;
    if (Buffer.isBuffer(data)) {
      if (data.length >= 2 && data[0] === 0xFF && data[1] === 0xFE) fileStr = data.toString("utf16le");
      else if (data.length >= 2 && data[0] === 0xFE && data[1] === 0xFF) fileStr = data.toString("utf16be");
      else fileStr = data.toString("utf8");
    } else {
      fileStr = data;
    }

    let fields = fileStr.match(/(?:"(.*?)[^\\]")|({)/g);
    if (!fields) { console.error("No fields found with regex."); return; }

    let index = -1;
    let counter = 0;
    let encryptVal = {};
    let decryptVal = {};

    fields.forEach(element => {
      if (element === "{") {
        index++;
        return;
      }
      counter++;
      let input = element.substring(1, element.length - 1);
      let decrypted = logResult(decrypt(luaStringToHex(input), index));
      encryptVal[counter] = input;
      decryptVal[counter] = decrypted;
    });

    let outdata = fileStr;
    for (let i = 1; i <= counter; i++) {
      if (encryptVal[i]) {
        logIt(encryptVal[i] + " = " + decryptVal[i], 0);
        outdata = outdata.replaceAll(encryptVal[i], decryptVal[i]);
      }
    }

    fs.writeFile(decodedGatewayFile, outdata, err => {
      if (err) console.error(err);
      else logIt("Wrote " + decodedGatewayFile, 0);
    });
  });
}

/* ----- helpers ----- */
function decimalToHex(d, padding) {
  var hex = Number(d).toString(16);
  padding = typeof padding === "undefined" ? 2 : padding;
  while (hex.length < padding) hex = "0" + hex;
  return hex;
}

function luaStringToHex(input) {
  logIt("Input: " + input, 1);
  let chars = input.split("");
  let codes = [];
  const special = ["a", "b", "f", "n", "r", "t", "v", "\\", "\"", "'", "[", "]"];
  const specialCodes = [7, 8, 12, 10, 13, 9, 11, 92, 34, 39, 91, 93];
  for (let i = 0; i < chars.length; i++) {
    let character, code, hex;
    let isEscape = chars[i] == "\\";
    if (i < chars.length && isEscape && special.includes(chars[i + 1])) {
      let next = specialCodes[special.indexOf(chars[i + 1])];
      character = chars[i] + chars[i + 1];
      code = parseFloat(next);
      hex = decimalToHex(next);
      codes.push(hex);
      i += 1;
    } else if (isEscape && !isNaN(parseFloat(chars[i + 1]))) {
      let nextChar = input.substring(i + 1, i + 4);
      character = input.substring(i + 0, i + 4);
      code = parseFloat(nextChar);
      hex = decimalToHex(nextChar);
      codes.push(hex);
      i += 3;
    } else {
      character = chars[i];
      code = input.charCodeAt(i);
      hex = code.toString(16).padStart(2, "0");
      codes.push(hex);
    }
    logIt("Char: " + (character + "   ").substring(0, 4) + " Code: " + (code + "  ").substring(0, 3) + " Hex: " + hex, 1);
  }
  return codes.join("");
}

/**
 * build IV by XORing index into ASCII base IV at positions 0,4,8,12
 */
function nextIV(index) {
  // base is ASCII codes of "0123456789012345"
  let base = Array.from(baseIVstr).map(c => c.charCodeAt(0));
  [0, 4, 8, 12].forEach(pos => { base[pos] ^= (index & 0xFF); });
  const hex = base.map(b => ("0" + (b & 0xFF).toString(16)).slice(-2)).join("");
  return CryptoJS.enc.Hex.parse(hex);
}

function decrypt(encrypted, index) {
  logIt("Encrypted(hex): " + encrypted, 1);
  var newIV = nextIV(index);
  config.iv = newIV;
  logIt("IV (hex): " + CryptoJS.enc.Hex.stringify(config.iv), 1);

  var aesDecryptor = CryptoJS.algo.AES.createDecryptor(key, config);
  var source = CryptoJS.enc.Hex.parse(encrypted);
  var decrypted = aesDecryptor.finalize(source);

  var hex = CryptoJS.enc.Hex.stringify(decrypted);
  var latin1 = CryptoJS.enc.Latin1.stringify(decrypted);
  logIt("Decrypted(hex): " + hex, 1);
  logIt("Decrypted(latin1): " + latin1, 1);
  return latin1;
}

/* choose mapping for type id. handle ascii-digit prefixes (e.g. '2' -> 50 -> convert to 2) */
function logResult(result) {
  var endIndex = result.length;
  var typeByte = result.charCodeAt(0);
  var typeId = (typeByte >= 48 && typeByte <= 57) ? (typeByte - 48) : typeByte;
  var payload = result.substring(1, endIndex);
  return mapType(typeId, payload);
}

function mapType(typeId, result) {
  switch (typeId) {
    case 1:
      // number handling: result is latin1; convert to hex bytes, then to number
      try {
        let hex = CryptoJS.enc.Hex.stringify(CryptoJS.enc.Latin1.parse(result));
        // remove trailing byte if padding-like
        if (hex.length > 2) hex = hex.substring(0, hex.length - 2);
        return Number("0x" + hex);
      } catch (e) {
        return "Number(parse-fail): " + result;
      }

    case 2:
      // string. clean trailing control bytes, try UTF-16LE fallback if many 0x00 bytes
      try {
        let rawLatin1 = result;
        // trim trailing 0x0B (vertical tab) which appears in some dumps
        let cleaned = rawLatin1.replace(/\x0B+$/g, "");
        // trim trailing NULs
        cleaned = cleaned.replace(/\x00+$/g, "");

        // prepare hex bytes for detection
        let hex = CryptoJS.enc.Hex.stringify(CryptoJS.enc.Latin1.parse(rawLatin1));
        let bytes = Buffer.from(hex, "hex");

        // heuristic: if many nulls in odd positions -> likely UTF-16LE
        let nullCount = 0;
        let checks = Math.min(Math.floor(bytes.length / 2), 10);
        for (let i = 1, cnt = 0; i < bytes.length && cnt < checks; i += 2, cnt++) {
          if (bytes[i] === 0) nullCount++;
        }

        if (nullCount >= Math.max(2, Math.floor(checks * 0.6))) {
          // try utf16le decode and pick whichever yields more printable chars
          let utf16;
          try { utf16 = bytes.toString("utf16le"); } catch (e) { utf16 = null; }
          if (utf16) {
            let utf16Score = countPrintable(utf16);
            let cleanedScore = countPrintable(cleaned);
            if (utf16Score > cleanedScore) {
              return utf16;
            }
          }
        }

        // final fallback: return cleaned latin1
        return cleaned;
      } catch (e) {
        return "String(parse-fail): " + result;
      }

    case 3:
      // boolean-ish; try parse numeric content
      try {
        let n = parseInt(result.replace(/\x00/g, ""), 16);
        return n ? true : false;
      } catch (e) {
        return "Boolean(parse-fail): " + result;
      }

    default:
      return "Unknown(" + typeId + "): " + result;
  }
}

function countPrintable(s) {
  if (!s) return 0;
  let m = s.match(/[ -~]/g); // printable ASCII
  return m ? m.length : 0;
}

function logIt(message, level) {
  if (logLevel >= level) console.log(message);
}
