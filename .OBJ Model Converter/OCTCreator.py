#BUILDDATE 10/2/25

import sys
import os
import argparse

# by cass

def create_oct_file(ibuf_filename, vbuf_filename, base_name):
    
    # filenames
    ibuf_basename = os.path.basename(ibuf_filename)
    vbuf_basename = os.path.basename(vbuf_filename)
    
    oct_content = f'''<?xml version="1.0" ?>
<root_node>
   <DisplayLayerPool>
      <DisplayLayer type="reference_string">
         0
         <Name type="string">_cull_default</Name>
         <Mask type="int8">-1</Mask>
      </DisplayLayer>
   </DisplayLayerPool>
   <MaterialBundlePool>
      <MaterialBundle type="reference_string">
         0
         <FileName type="string">{base_name}.mtb</FileName>
      </MaterialBundle>
   </MaterialBundlePool>
   <MaterialPool>
      <Material type="reference_string">
         0
         <Name type="string">lambert1</Name>
         <FileName type="string">maya.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
   </MaterialPool>
   <VertexBufferPool>
      <VertexBuffer type="reference_string">
         0
         <Name type="string">Static</Name>
         <Flags type="int8">73</Flags>
         <Size type="uint16">14112</Size>
         <HeapLoc type="int8">0</HeapLoc>
         <FileName type="string">{vbuf_basename}</FileName>
      </VertexBuffer>
      <VertexBuffer type="reference_string">
         1
         <Name type="string">Dynamic</Name>
         <Flags type="int8">127</Flags>
         <Size type="int8">0</Size>
         <HeapLoc type="int8">0</HeapLoc>
      </VertexBuffer>
   </VertexBufferPool>
   <IndexBufferPool>
      <IndexBuffer type="reference_string">
         0
         <Width type="int8">2</Width>
         <Name type="string">Static</Name>
         <Flags type="int8">91</Flags>
         <Size type="uint16">4800</Size>
         <FileName type="string">{ibuf_basename}</FileName>
      </IndexBuffer>
      <IndexBuffer type="reference_string">
         1
         <Width type="int8">2</Width>
         <Name type="string">Dynamic</Name>
         <Flags type="int8">127</Flags>
         <Size type="int8">0</Size>
      </IndexBuffer>
      <IndexBuffer type="reference_string">
         2
         <Width type="int8">4</Width>
         <Name type="string">Static</Name>
         <Flags type="int8">91</Flags>
         <Size type="int8">0</Size>
      </IndexBuffer>
      <IndexBuffer type="reference_string">
         3
         <Width type="int8">4</Width>
         <Name type="string">Dynamic</Name>
         <Flags type="int8">127</Flags>
         <Size type="int8">0</Size>
      </IndexBuffer>
      <IndexBuffer type="reference_string">
         4
         <Width type="int8">1</Width>
         <Name type="string">Static</Name>
         <Flags type="int8">91</Flags>
         <Size type="int8">0</Size>
      </IndexBuffer>
      <IndexBuffer type="reference_string">
         5
         <Width type="int8">1</Width>
         <Name type="string">Dynamic</Name>
         <Flags type="int8">127</Flags>
         <Size type="int8">0</Size>
      </IndexBuffer>
   </IndexBufferPool>
   <SceneTreeNodePool>
      <Node type="reference_string">
         0
         <Type type="string">Scene</Type>
      </Node>
      <Node type="reference_string">
         1
         <NodeName type="string">{base_name}</NodeName>
         <Uuid type="uint8_list">
            <entry>231</entry>
            <entry>138</entry>
            <entry>97</entry>
            <entry>87</entry>
            <entry>163</entry>
            <entry>171</entry>
            <entry>87</entry>
            <entry>67</entry>
            <entry>183</entry>
            <entry>207</entry>
            <entry>177</entry>
            <entry>187</entry>
            <entry>203</entry>
            <entry>152</entry>
            <entry>54</entry>
            <entry>56</entry>
         </Uuid>
         <DisplayLayer type="int8">-1</DisplayLayer>
         <Type type="string">Geometry</Type>
         <Visible type="int8">1</Visible>
         <DynamicVisPlacement type="int8">1</DynamicVisPlacement>
         <MeshName type="string">{base_name}:{base_name}Shape</MeshName>
         <BoundingSphereCenter type="float_list">
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>-4.172325134277344e-07</entry>
         </BoundingSphereCenter>
         <BoundingSphereRadius type="float">1.500001072883606</BoundingSphereRadius>
         <BoundingOBBOrientation type="float_list">
            <entry>1.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>1.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>1.0</entry>
         </BoundingOBBOrientation>
         <BoundingOBBCenter type="float_list">
            <entry>-7.748603536583687e-09</entry>
            <entry>5.2899120639438024e-09</entry>
            <entry>-3.661215259853634e-07</entry>
         </BoundingOBBCenter>
         <BoundingOBBExtents type="float_list">
            <entry>1.5</entry>
            <entry>0.5</entry>
            <entry>1.5000004768371582</entry>
         </BoundingOBBExtents>
         <BoundingBox type="float_list">
            <entry>-1.5</entry>
            <entry>-0.5</entry>
            <entry>-1.5000008344650269</entry>
            <entry>1.5</entry>
            <entry>0.5</entry>
            <entry>1.5</entry>
         </BoundingBox>
         <BoundingType type="string">Box</BoundingType>
         <NumPrimitives type="int8">1</NumPrimitives>
         <Primitives>
            <Primitive type="reference_string">
               0
               <MaterialName type="string">maya</MaterialName>
               <MaterialReference type="int8">0</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="uint16_list">
                  <entry>0</entry>
                  <entry>0</entry>
                  <entry>0</entry>
                  <entry>2400</entry>
               </Idata>
               <Vdata type="uint16_list">
                  <entry>2</entry>
                  <entry>441</entry>
                  <entry>0</entry>
                  <entry>0</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>7056</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
         </Primitives>
         <ParentNodeReferences type="int8_list">
            <entry>0</entry>
         </ParentNodeReferences>
         <LocalToParentMatrix type="float_list">
            <entry>1.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>1.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>1.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>0.0</entry>
            <entry>1.0</entry>
         </LocalToParentMatrix>
      </Node>
   </SceneTreeNodePool>
   <AssetPool>
      <Asset type="reference_string">
         0
         <Name type="string">Root</Name>
         <SubNetworkRef type="int8">0</SubNetworkRef>
         <SceneTreeNodeRef type="int8">0</SceneTreeNodeRef>
         <AggregateCount type="int8">0</AggregateCount>
      </Asset>
   </AssetPool>
   <ExporterDate type="string">Feb 22 2012</ExporterDate>
   <ExporterTime type="string">12:41:15</ExporterTime>
</root_node>'''

    return oct_content

def save_oct_file(ibuf_filename, vbuf_filename, base_name, filename=None):
    # Save it
    if filename is None:
        filename = f"{base_name}.oct"
    
    content = create_oct_file(ibuf_filename, vbuf_filename, base_name)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[OCTCreator] .OCT file saved as: {filename}")

def main():
    parser = argparse.ArgumentParser(description='.OCT File Creator for Disney Infinity Models')
    parser.add_argument('--ibuf', required=True, help='Input .IBUF filename')
    parser.add_argument('--vbuf', required=True, help='Input .VBUF filename') 
    parser.add_argument('--base', required=True, help='Base name for the model')
    parser.add_argument('--output', help='Output .OCT filename (optional)')
    
    args = parser.parse_args()
    
    print("===========Disney Infinity 3.0 Gold Edition .OCT Creator============")
    print(f"[OCTCreator] Creating .OCT file for: {args.base}")
    print(f"[OCTCreator] Using .IBUF: {args.ibuf}")
    print(f"[OCTCreator] Using .VBUF: {args.vbuf}")
    
    save_oct_file(args.ibuf, args.vbuf, args.base, args.output)
    print("[OCTCreator] .OCT creation completed successfully!")
    print("[WARNING!!!] YOU HAVE TO RE-ENCODE YOUR .OCT WITH C2DITools, PROVIDED IN DIMT!")
    print("===================================================================")

if __name__ == "__main__":
    main()