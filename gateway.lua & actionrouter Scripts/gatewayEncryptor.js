/*
 * DisneyInfinity Gateway ENCRYPTOR
 *
 * Author: Cassinni4 and JiroTheOne
 * 
 * THE DECRYPTION SCRIPT IS BROKEN PLEASE FOR THE LOVE OF FUCK USE THE OLD ONE!!!!!!!!!!
 * To run:
 * - Install node.js and crypto-js and fs
 * - Run node gatewayCrypto.js
 *
 */
const CryptoJS = require("crypto-js");
const fs = require('fs');
const logLevel = 1; // 0 = silent, 1 = show encrypt logs


/*=================== Basic Settings ===================*/
const sourceGatewayFile = 'gateway.lua.txt';
const decodedGatewayFile = 'gateway_undecrypted.txt';

/*=============== Encryption Settings ==================*/
const key = CryptoJS.enc.Hex.parse("000102030405060708090a0b0c0d0e0f"); //FROM CASSINNI. Never change these lol. Or do.
const iv = CryptoJS.enc.Utf8.parse("0123456789012345");

var config = { 
  iv: iv,
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7 // Seems to give cleaner output than NoPadding or ZeroPadding when decrypting
};

function mapType(typeId, payload) {
  if (typeId === 2) {
    return "String(" + payload + ")";
  }
  // fallback
  return "Unknown(" + typeId +"): " + payload;
}

function logResult(result) {
  var endIndex = result.length;
  // not sure about this it was helping to remove trailing garbage chars
  /*
  for (var i = result.length - 1 ; i >= 0; i--) {
    if (result.charCodeAt(i) != 11) {
      endIndex = i+1;
      break;
    }
  }*/
  return mapType(result.charCodeAt(0), result.substring(1, endIndex));
}

function decryptGateway() {
	var fields;

	fs.readFile(sourceGatewayFile, 'utf8' , (err, data) => {
		if (err) {
			console.error(err);
			return;
		}
		//console.log(data)
		//fields = data.match(/"(.*?)[^\\]"/g);
		fields = data.match(/(?:"(.*?)[^\\]")|({)/g); // capture opening { so we have an index for the IV
		var 
			header = data.substring(0, 40);
		// find the IV block index so we can isolate the cipher text properly
		var ivIndex = fields.indexOf("{");
		// the IV text is the next item after that opening brace
		var ivText = fields[ivIndex + 1];
		ivText = ivText.replace(/^"|"$/g, "");
		ivText = ivText.replace(/\\\n/g, "");
		ivText = ivText.replace(/\\\}/g, "}");
		// the encoded stuff follows later, capture it
		var raw = data.substring(data.indexOf(ivText) + ivText.length);
		// strip padding cruft if necessary
		// crude cleanup: pick everything after the IV text to the end and try to find trailing " characters
		var idx = raw.lastIndexOf('"');
		if (idx != -1) {
			raw = raw.substring(0, idx);
		}
		raw = raw.trim();
		// now decrypt the captured hex string
		var cipherHex = raw.replace(/[^0-9a-fA-F]/g, "");
		if (!cipherHex || cipherHex.length === 0) {
			console.error("No cipher text found.");
			return;
		}
		try {
			var cipherParams = CryptoJS.lib.CipherParams.create({
				ciphertext: CryptoJS.enc.Hex.parse(cipherHex)
			});
			var decrypted = CryptoJS.AES.decrypt(cipherParams, key, config);
			var result = decrypted.toString(CryptoJS.enc.Utf8);
			console.log("Decrypted result raw: ", result);
			console.log("Interpreted:", logResult(result));
		} catch (e) {
			console.error("Decryption failed: ", e);
		}
	});
}

/* ===================== Encryption =======================
   encrypt(plaintext) should produce exactly the same format
   that the decrypt routine expects: a hex string representing
   the AES-CBC(PKCS7) ciphertext. The original implementation
   parsed the plaintext as hex incorrectly. The gateway expects
   a leading type byte (0x02 for strings) followed by the
   payload bytes. This function handles both raw plaintext
   (UTF-8) and raw-hex payloads.
======================================================== */
function encrypt(plaintext) {
	// Accept either hex input or plain UTF-8 text.
	// Prepend a single type byte 0x02 as the original code expected.
	let wordData;
	// If plaintext is exclusively hex characters and even length treat it as raw hex bytes.
	if (/^[0-9a-fA-F]+$/.test(plaintext) && (plaintext.length % 2) === 0) {
		let payloadHex = "02" + plaintext;
		wordData = CryptoJS.enc.Hex.parse(payloadHex);
	} else {
		// prefix with byte 0x02 then UTF-8 encode
		let prefixed = String.fromCharCode(2) + plaintext;
		wordData = CryptoJS.enc.Utf8.parse(prefixed);
	}
	// Use high level API to ensure proper IV/mode/padding are applied.
	let encrypted = CryptoJS.AES.encrypt(wordData, key, config);
	let hexEncrypted = encrypted.ciphertext.toString(CryptoJS.enc.Hex);
	logIt(plaintext + " = " + hexEncrypted, 0);
	return hexEncrypted;
}

function logIt(message, level) {
	if (logLevel >= level) {
		console.log(message);
	}
}

if (require.main === module) {
  const args = process.argv.slice(2);
  const cmd  = args[0];
  const data = args[1];

  if (!cmd || !data) {
    console.log("Usage:");
    console.log("  node gatewayCrypto.js encrypt \"plaintext or hex\"");
    //console.log("  node gatewayCrypto.js decrypt \"hexstring\"");
    process.exit(1);
  }

  if (cmd === "encrypt") {
    console.log(encrypt(data));
  } else if (cmd === "decrypt") {
    // reuse existing decrypt logic on a single string
    try {
      const cipherParams = CryptoJS.lib.CipherParams.create({
        ciphertext: CryptoJS.enc.Hex.parse(data)
      });
      const decrypted = CryptoJS.AES.decrypt(cipherParams, key, config);
      const result = decrypted.toString(CryptoJS.enc.Utf8);
      console.log(result);
    } catch (e) {
      console.error("Decrypt failed:", e);
    }
  } else {
    console.log("Unknown command:", cmd);
  }
}

