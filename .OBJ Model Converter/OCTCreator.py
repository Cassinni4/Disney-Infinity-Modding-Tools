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
   <SubNetworkPool>
      <SubNetwork type="reference_string">
         0
         <Type type="string">Scene</Type>
         <Name type="string">Scene</Name>
         <ConstantHeaderCount type="int8">0</ConstantHeaderCount>
         <VariableHeaderCount type="int8">9</VariableHeaderCount>
         <ConstantDataNodeCount type="int8">0</ConstantDataNodeCount>
         <VariableDataNodeCount type="int8">5</VariableDataNodeCount>
         <ProcessorNodeCount type="int8">2</ProcessorNodeCount>
         <VariableAccumulatedSize32>
            <__1 type="uint16_list">
               <entry>4</entry>
               <entry>184</entry>
               <entry>7</entry>
            </__1>
            <__4 type="int8_list">
               <entry>4</entry>
               <entry>12</entry>
               <entry>2</entry>
            </__4>
         </VariableAccumulatedSize32>
         <VariableAccumulatedSize64>
            <__1 type="uint16_list">
               <entry>8</entry>
               <entry>208</entry>
               <entry>7</entry>
            </__1>
            <__4 type="int8_list">
               <entry>8</entry>
               <entry>24</entry>
               <entry>2</entry>
            </__4>
         </VariableAccumulatedSize64>
         <BasisCount type="int8">2</BasisCount>
         <BasisConversionCount type="int8">2</BasisConversionCount>
         <ComponentFamilyCount type="int8">0</ComponentFamilyCount>
         <ComponentMemberCount type="int8">0</ComponentMemberCount>
         <VariantGroupCount type="int8">1</VariantGroupCount>
         <VariantMemberCount type="int8">2</VariantMemberCount>
         <LayerBindCount type="int8">0</LayerBindCount>
         <BaseDataNodeLinksCount type="int8">0</BaseDataNodeLinksCount>
         <BasisPool>
            <Basis type="reference_string">
               0
               <Type type="string">Geometry3d</Type>
               <Behavior type="string">Root</Behavior>
            </Basis>
            <Basis type="reference_string">
               1
               <Name type="string">Anchor</Name>
               <ParentRef type="int8">0</ParentRef>
               <Behavior type="string">Normal</Behavior>
            </Basis>
            <Basis type="reference_string">
               2
               <Type type="string">Visibility</Type>
               <Behavior type="string">Root</Behavior>
            </Basis>
            <Basis type="reference_string">
               3
               <Name type="string">Anchor</Name>
               <ParentRef type="int8">2</ParentRef>
               <Behavior type="string">Normal</Behavior>
            </Basis>
         </BasisPool>
         <HeaderStrings type="string_list">
            <entry>In WorldBasis.Transform</entry>
            <entry>Anchor</entry>
            <entry>Transform</entry>
            <entry>Castle_Whole1</entry>
            <entry>ConvertDilationToTransform</entry>
            <entry>Convert To WorldBasis</entry>
            <entry>Visibility</entry>
            <entry>In WorldBasis</entry>
         </HeaderStrings>
         <HeaderStringIndices type="int8_list">
            <entry>1</entry>
            <entry>6</entry>
            <entry>2</entry>
            <entry>3</entry>
            <entry>2</entry>
            <entry>0</entry>
            <entry>7</entry>
            <entry>5</entry>
            <entry>4</entry>
         </HeaderStringIndices>
         <HeaderLayout type="int8_list">
            <entry>0</entry>
            <entry>1</entry>
            <entry>1</entry>
            <entry>3</entry>
            <entry>4</entry>
            <entry>1</entry>
            <entry>5</entry>
            <entry>3</entry>
            <entry>6</entry>
            <entry>1</entry>
         </HeaderLayout>
         <ConstantLayoutCount type="int8">0</ConstantLayoutCount>
         <DataNodePool>
            <DataNode type="reference_string">
               0
               <Header type="int8">2</Header>
               <Type type="string">Visibility</Type>
               <External type="int8">1</External>
               <BasisRef type="int8">2</BasisRef>
               <Data type="int8">0</Data>
            </DataNode>
            <DataNode type="reference_string">
               1
               <Header type="int8">3</Header>
               <Type type="string">Dilation</Type>
               <External type="int8">1</External>
               <BasisRef type="int8">0</BasisRef>
            </DataNode>
            <DataNode type="reference_string">
               2
               <Header type="int8">5</Header>
               <Type type="string">Dilation</Type>
               <External type="int8">1</External>
               <BasisRef type="int8">1</BasisRef>
            </DataNode>
            <DataNode type="reference_string">
               3
               <Header type="int8">6</Header>
               <Type type="string">Transform</Type>
               <External type="int8">1</External>
               <BasisRef type="int8">0</BasisRef>
               <Data>
                  <Translation type="float_list">
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                  </Translation>
                  <Orientation type="float_list">
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                     <entry>1.0</entry>
                  </Orientation>
                  <Scale type="float_list">
                     <entry>1.0</entry>
                     <entry>1.0</entry>
                     <entry>1.0</entry>
                     <entry>1.0</entry>
                  </Scale>
                  <Unscale type="float_list">
                     <entry>1.0</entry>
                     <entry>1.0</entry>
                     <entry>1.0</entry>
                     <entry>1.0</entry>
                  </Unscale>
               </Data>
            </DataNode>
            <DataNode type="reference_string">
               4
               <Header type="int8">7</Header>
               <Type type="string">Dilation</Type>
               <BasisRef type="int8">0</BasisRef>
               <Data>
                  <Translation type="float_list">
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                  </Translation>
                  <Orientation type="float_list">
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                     <entry>0.0</entry>
                     <entry>1.0</entry>
                  </Orientation>
                  <Scale type="float">1.0</Scale>
               </Data>
            </DataNode>
         </DataNodePool>
         <ComponentFamilyPool/>
         <BasisConversionPool>
            <BasisConversion>
               <FromBasisRef type="int8">1</FromBasisRef>
               <ToBasisRef type="int8">0</ToBasisRef>
               <DataNodeRef type="int8">1</DataNodeRef>
            </BasisConversion>
            <BasisConversion>
               <FromBasisRef type="int8">3</FromBasisRef>
               <ToBasisRef type="int8">2</ToBasisRef>
               <DataNodeRef type="int8">0</DataNodeRef>
            </BasisConversion>
         </BasisConversionPool>
         <ProcessorNodePool>
            <ProcessorNode type="reference_string">
               0
               <Header type="int8">9</Header>
               <Type type="string">DilationToTransformVariantProcessor</Type>
               <DataNodeRefs type="int8_list">
                  <entry>4</entry>
                  <entry>3</entry>
               </DataNodeRefs>
               <DataNodeAttributes type="string_list">
                  <entry>Input</entry>
                  <entry>Output</entry>
               </DataNodeAttributes>
            </ProcessorNode>
            <ProcessorNode type="reference_string">
               1
               <Header type="int8">8</Header>
               <Type type="string">TransformDilationWithDilation</Type>
               <DataNodeRefs type="int8_list">
                  <entry>2</entry>
                  <entry>1</entry>
                  <entry>4</entry>
               </DataNodeRefs>
               <DataNodeAttributes type="string_list">
                  <entry>Input</entry>
                  <entry>Converter</entry>
                  <entry>Output</entry>
               </DataNodeAttributes>
            </ProcessorNode>
         </ProcessorNodePool>
         <VariantGroupPool>
            <VariantGroup type="int8_list">
               <entry>4</entry>
               <entry>3</entry>
            </VariantGroup>
         </VariantGroupPool>
      </SubNetwork>
   </SubNetworkPool>
   <CollisionShapePool>
      <Shape type="reference_string">
         0
         <ShapeType type="string">Box</ShapeType>
         <SurfaceType type="int8">0</SurfaceType>
         <Extent type="float_list">
            <entry>94.0</entry>
            <entry>58.0</entry>
            <entry>52.0</entry>
         </Extent>
      </Shape>
      <Shape type="reference_string">
         1
         <ShapeType type="string">Compound</ShapeType>
         <Shapes>
            <Shape type="reference_string">
               0
               <ShapeRef type="int8">0</ShapeRef>
               <Transform type="float_list">
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
                  <entry>58.0</entry>
                  <entry>6.0</entry>
                  <entry>1.0</entry>
               </Transform>
            </Shape>
         </Shapes>
      </Shape>
   </CollisionShapePool>
   <CollisionInstancePool>
      <Instance type="reference_string">
         0
         <Transform type="float_list">
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
         </Transform>
         <Friction type="float">0.800000011920929</Friction>
         <Restitution type="float">0.20000000298023224</Restitution>
      </Instance>
   </CollisionInstancePool>
   <DisplayLayerPool>
      <DisplayLayer type="reference_string">
         0
         <Name type="string">_cull_default</Name>
         <Mask type="int8">-1</Mask>
      </DisplayLayer>
   </DisplayLayerPool>
   <CellPool>
      <Cell type="reference_string">
         0
         <Name type="string">_REST_OF_WORLD_</Name>
         <Flags type="int8">3</Flags>
         <BoundingBox type="float_list">
            <entry>-3.4028234663852886e+38</entry>
            <entry>-3.4028234663852886e+38</entry>
            <entry>-3.4028234663852886e+38</entry>
            <entry>3.4028234663852886e+38</entry>
            <entry>3.4028234663852886e+38</entry>
            <entry>3.4028234663852886e+38</entry>
         </BoundingBox>
         <CellToWorldMatrix type="float_list">
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
         </CellToWorldMatrix>
      </Cell>
   </CellPool>
   <MaterialBundlePool>
      <MaterialBundle type="reference_string">
         0
         <FileName type="string">{base_name}.mtb</FileName>
      </MaterialBundle>
   </MaterialBundlePool>
   <MaterialPool>
      <Material type="reference_string">
         0
         <Name type="string">_mayaBuffer_rr_inc_concrete_dark2_Lambert</Name>
         <FileName type="string">materials__worlds__rr_inc_concrete_dark2.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         1
         <Name type="string">_mayaBuffer_rr_bridge_rope_Lambert</Name>
         <FileName type="string">materials__worlds__rr_bridge_rope.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         2
         <Name type="string">_mayaBuffer_rr_dc_smallbrickalpha</Name>
         <FileName type="string">materials__worlds__rr_dc_smallbrickalpha.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         3
         <Name type="string">_mayaBuffer_rr_inc_concrete_medium2_Lambert</Name>
         <FileName type="string">materials__worlds__rr_inc_concrete_medium2.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         4
         <Name type="string">_mayaBuffer_rr_dc_largebrick2</Name>
         <FileName type="string">materials__worlds__rr_dc_largebrick2.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         5
         <Name type="string">_mayaBuffer_rr_squarecobblestone</Name>
         <FileName type="string">materials__worlds__rr_squarecobblestone.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         6
         <Name type="string">_mayaBuffer_RR_DC_CastleWallChunk</Name>
         <FileName type="string">materials__worlds__rr_dc_castlewallchunk.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         7
         <Name type="string">_mayaBuffer_RR_DC_CastleBlue_lighter_Lambert</Name>
         <FileName type="string">materials__worlds__rr_dc_castleblue_lighter.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         8
         <Name type="string">rr_toy_wood2</Name>
         <FileName type="string">materials__worlds__rr_toy_wood2.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         9
         <Name type="string">_mayaBuffer_rr_dc_goldflake_Lambert</Name>
         <FileName type="string">materials__worlds__rr_dc_goldflake.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         10
         <Name type="string">_mayaBuffer_rr_toy_yellowlens_glow3</Name>
         <FileName type="string">materials__worlds__rr_toy_yellowlens_glow3.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         11
         <Name type="string">_mayaBuffer_rr_dc_castleflag</Name>
         <FileName type="string">materials__worlds__rr_dc_castleflag.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         12
         <Name type="string">_mayaBuffer_rr_dc_tricirclewindow</Name>
         <FileName type="string">materials__worlds__rr_dc_tricirclewindow.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         13
         <Name type="string">_mayaBuffer_rr_toy_plastic_black_Lambert</Name>
         <FileName type="string">materials__worlds__rr_toy_plastic_black.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         14
         <Name type="string">_mayaBuffer_rr_dc_flatrooftile</Name>
         <FileName type="string">materials__worlds__rr_dc_flatrooftile.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         15
         <Name type="string">lambert1</Name>
         <FileName type="string">maya.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         16
         <Name type="string">_mayaBuffer_rr_dc_squarewindow</Name>
         <FileName type="string">materials__worlds__rr_dc_squarewindow.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         17
         <Name type="string">_mayaBuffer_rr_dc_castleblueshingle_Lambert</Name>
         <FileName type="string">materials__worlds__rr_dc_castleblueshingle.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         18
         <Name type="string">rr_inc_concrete_dark</Name>
         <FileName type="string">materials__worlds__rr_inc_concrete_dark.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         19
         <Name type="string">_mayaBuffer_rr_toy_plastic_white_Lambert</Name>
         <FileName type="string">materials__worlds__rr_toy_plastic_white.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
      <Material type="reference_string">
         20
         <Name type="string">_mayaBuffer_proto_metal</Name>
         <FileName type="string">mats_world__blockout_surfaces__tums__proto_metal.mtl</FileName>
         <Type type="string">Shader</Type>
         <Effect type="string"/>
         <PropertyEntries/>
      </Material>
   </MaterialPool>
   <VertexBufferPool>
      <VertexBuffer type="reference_string">
         0
         <Name type="string">Static</Name>
         <Flags type="int8">91</Flags>
         <Size type="int24">1900000</Size>
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
         <Size type="int24">1500000</Size>
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
         <NodeName type="string">Anchor</NodeName>
         <Uuid type="uint8_list">
            <entry>100</entry>
            <entry>64</entry>
            <entry>98</entry>
            <entry>163</entry>
            <entry>128</entry>
            <entry>95</entry>
            <entry>86</entry>
            <entry>79</entry>
            <entry>189</entry>
            <entry>125</entry>
            <entry>117</entry>
            <entry>84</entry>
            <entry>141</entry>
            <entry>245</entry>
            <entry>91</entry>
            <entry>11</entry>
         </Uuid>
         <DisplayLayer type="int8">-1</DisplayLayer>
         <Type type="string">Transform</Type>
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
      <Node type="reference_string">
         2
         <NodeName type="string">Castle_Whole1</NodeName>
         <Uuid type="uint8_list">
            <entry>130</entry>
            <entry>48</entry>
            <entry>89</entry>
            <entry>93</entry>
            <entry>247</entry>
            <entry>64</entry>
            <entry>40</entry>
            <entry>72</entry>
            <entry>144</entry>
            <entry>44</entry>
            <entry>88</entry>
            <entry>180</entry>
            <entry>186</entry>
            <entry>84</entry>
            <entry>147</entry>
            <entry>211</entry>
         </Uuid>
         <DisplayLayer type="int8">-1</DisplayLayer>
         <Type type="string">Geometry</Type>
         <Visible type="int8">1</Visible>
         <DynamicVisPlacement type="int8">1</DynamicVisPlacement>
         <MeshName type="string">Castle_Whole1Shape</MeshName>
         <BoundingSphereCenter type="float_list">
            <entry>0.0</entry>
            <entry>57.030540466308594</entry>
            <entry>6.122894287109375</entry>
         </BoundingSphereCenter>
         <BoundingSphereRadius type="float">109.20896911621094</BoundingSphereRadius>
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
            <entry>-1.6689300537109375e-06</entry>
            <entry>57.030540466308594</entry>
            <entry>6.122893810272217</entry>
         </BoundingOBBCenter>
         <BoundingOBBExtents type="float_list">
            <entry>93.85595703125</entry>
            <entry>57.04289245605469</entry>
            <entry>52.039669036865234</entry>
         </BoundingOBBExtents>
         <BoundingBox type="float_list">
            <entry>-93.85595703125</entry>
            <entry>-0.012353578582406044</entry>
            <entry>-45.91677474975586</entry>
            <entry>93.85595703125</entry>
            <entry>114.07343292236328</entry>
            <entry>58.16256332397461</entry>
         </BoundingBox>
         <BoundingType type="string">Box</BoundingType>
         <NumPrimitives type="int8">21</NumPrimitives>
         <Primitives>
            <Primitive type="reference_string">
               0
               <MaterialName type="string">materials__worlds__rr_inc_concrete_dark2</MaterialName>
               <MaterialReference type="int8">0</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="uint16_list">
                  <entry>0</entry>
                  <entry>0</entry>
                  <entry>0</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>5474</entry>
                  <entry>0</entry>
                  <entry>0</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>678816</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1356480</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               1
               <MaterialName type="string">materials__worlds__rr_bridge_rope</MaterialName>
               <MaterialReference type="int8">1</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="uint16_list">
                  <entry>0</entry>
                  <entry>20124</entry>
                  <entry>5474</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>744</entry>
                  <entry>0</entry>
                  <entry>87584</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>766400</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               2
               <MaterialName type="string">materials__worlds__rr_dc_smallbrickalpha</MaterialName>
               <MaterialReference type="int8">2</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="uint16_list">
                  <entry>0</entry>
                  <entry>25308</entry>
                  <entry>6218</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>1861</entry>
                  <entry>0</entry>
                  <entry>99488</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>778304</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               3
               <MaterialName type="string">materials__worlds__rr_inc_concrete_medium2</MaterialName>
               <MaterialReference type="int8">3</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>31170</entry>
                  <entry>8079</entry>
                  <entry>62027</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>60000</entry>
                  <entry>0</entry>
                  <entry>129264</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>808080</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1378376</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               4
               <MaterialName type="string">materials__worlds__rr_dc_largebrick2</MaterialName>
               <MaterialReference type="int8">4</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>115224</entry>
                  <entry>29245</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>3354</entry>
                  <entry>0</entry>
                  <entry>467920</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1146736</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1463040</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               5
               <MaterialName type="string">materials__worlds__rr_squarecobblestone</MaterialName>
               <MaterialReference type="int8">5</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>130092</entry>
                  <entry>32599</entry>
                  <entry>100000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>445</entry>
                  <entry>0</entry>
                  <entry>521584</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1200400</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1476456</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               6
               <MaterialName type="string">materials__worlds__rr_dc_castlewallchunk</MaterialName>
               <MaterialReference type="int8">6</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>131730</entry>
                  <entry>33044</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>1714</entry>
                  <entry>0</entry>
                  <entry>528704</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1207520</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1478236</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               7
               <MaterialName type="string">materials__worlds__rr_dc_castleblue_lighter</MaterialName>
               <MaterialReference type="int8">7</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>138066</entry>
                  <entry>34758</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>194</entry>
                  <entry>0</entry>
                  <entry>556128</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1234944</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               8
               <MaterialName type="string">materials__worlds__rr_toy_wood2</MaterialName>
               <MaterialReference type="int8">8</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>138672</entry>
                  <entry>34952</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>1012</entry>
                  <entry>0</entry>
                  <entry>559232</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1238048</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1485092</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               9
               <MaterialName type="string">materials__worlds__rr_dc_goldflake</MaterialName>
               <MaterialReference type="int8">9</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>141960</entry>
                  <entry>35964</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>3106</entry>
                  <entry>0</entry>
                  <entry>575424</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1254240</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               10
               <MaterialName type="string">materials__worlds__rr_toy_yellowlens_glow3</MaterialName>
               <MaterialReference type="int8">10</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>152724</entry>
                  <entry>39070</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>720</entry>
                  <entry>0</entry>
                  <entry>625120</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1303936</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               11
               <MaterialName type="string">materials__worlds__rr_dc_castleflag</MaterialName>
               <MaterialReference type="int8">11</MaterialReference>
               <vformatCRC type="uint32">2850331088</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>154884</entry>
                  <entry>39790</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>288</entry>
                  <entry>0</entry>
                  <entry>636640</entry>
                  <entry>20</entry>
                  <entry>0</entry>
                  <entry>1315456</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               12
               <MaterialName type="string">materials__worlds__rr_dc_tricirclewindow</MaterialName>
               <MaterialReference type="int8">12</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>156528</entry>
                  <entry>40078</entry>
                  <entry>30000</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>300</entry>
                  <entry>0</entry>
                  <entry>642400</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1320064</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1489140</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               13
               <MaterialName type="string">materials__worlds__rr_toy_plastic_black</MaterialName>
               <MaterialReference type="int8">13</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>157500</entry>
                  <entry>40378</entry>
                  <entry>453</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>309</entry>
                  <entry>0</entry>
                  <entry>647200</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1324864</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               14
               <MaterialName type="string">materials__worlds__rr_dc_flatrooftile</MaterialName>
               <MaterialReference type="int8">14</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>158406</entry>
                  <entry>40687</entry>
                  <entry>222</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>132</entry>
                  <entry>0</entry>
                  <entry>652144</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1329808</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1490340</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               15
               <MaterialName type="string">maya</MaterialName>
               <MaterialReference type="int8">15</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>158850</entry>
                  <entry>40819</entry>
                  <entry>3</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>3</entry>
                  <entry>0</entry>
                  <entry>654256</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1331920</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               16
               <MaterialName type="string">materials__worlds__rr_dc_squarewindow</MaterialName>
               <MaterialReference type="int8">16</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>158856</entry>
                  <entry>40822</entry>
                  <entry>816</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>544</entry>
                  <entry>0</entry>
                  <entry>654304</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1331968</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               17
               <MaterialName type="string">materials__worlds__rr_dc_castleblueshingle</MaterialName>
               <MaterialReference type="int8">17</MaterialReference>
               <vformatCRC type="uint32">446304473</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>160488</entry>
                  <entry>41366</entry>
                  <entry>1152</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>3</entry>
                  <entry>390</entry>
                  <entry>0</entry>
                  <entry>663008</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1340672</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1490868</entry>
                  <entry>4</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               18
               <MaterialName type="string">materials__worlds__rr_inc_concrete_dark</MaterialName>
               <MaterialReference type="int8">18</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>162792</entry>
                  <entry>41756</entry>
                  <entry>6</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>4</entry>
                  <entry>0</entry>
                  <entry>669248</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1346912</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               19
               <MaterialName type="string">materials__worlds__rr_toy_plastic_white</MaterialName>
               <MaterialReference type="int8">19</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>162804</entry>
                  <entry>41760</entry>
                  <entry>462</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>306</entry>
                  <entry>0</entry>
                  <entry>669312</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1346976</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
            <Primitive type="reference_string">
               20
               <MaterialName type="string">mats_world__blockout_surfaces__tums__proto_metal</MaterialName>
               <MaterialReference type="int8">20</MaterialReference>
               <vformatCRC type="uint32">1672376591</vformatCRC>
               <RenderCaps type="uint16">512</RenderCaps>
               <BillboardType type="int8">-1</BillboardType>
               <OcclusionType type="int8">0</OcclusionType>
               <OcclusionCheckRadius type="float">0.25</OcclusionCheckRadius>
               <OcclusionFadeKp type="float">0.10000000149011612</OcclusionFadeKp>
               <Idata type="int24_list">
                  <entry>0</entry>
                  <entry>163728</entry>
                  <entry>42066</entry>
                  <entry>828</entry>
               </Idata>
               <Vdata type="int24_list">
                  <entry>2</entry>
                  <entry>288</entry>
                  <entry>0</entry>
                  <entry>674208</entry>
                  <entry>16</entry>
                  <entry>0</entry>
                  <entry>1351872</entry>
                  <entry>16</entry>
               </Vdata>
            </Primitive>
         </Primitives>
         <ParentNodeReferences type="int8_list">
            <entry>1</entry>
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
         <AggregateCount type="int8">1</AggregateCount>
      </Asset>
   </AssetPool>
   <AssociationPool>
      <Association type="reference_string">
         0
         <NodeName type="string">Anchor|Castle_Whole1</NodeName>
         <Type type="string">CollisionInstanceToSceneTreeNode</Type>
         <CollisionInstanceRef type="int8">0</CollisionInstanceRef>
         <SceneTreeNodeRef type="int8">2</SceneTreeNodeRef>
      </Association>
      <Association type="reference_string">
         1
         <NodeName type="string">Anchor|Castle_Whole1|Transform|In WorldBasis.Transform</NodeName>
         <Type type="string">CollisionInstanceToDataNode</Type>
         <SubNetworkRef type="int8">0</SubNetworkRef>
         <CollisionInstanceRef type="int8">0</CollisionInstanceRef>
         <AssetIndex type="int8">0</AssetIndex>
      </Association>
      <Association type="reference_string">
         2
         <NodeName type="string">Anchor|Castle_Whole1|Transform|In WorldBasis.Transform</NodeName>
         <Type type="string">CollisionAggregate</Type>
         <CollisionInstanceRef type="int8">0</CollisionInstanceRef>
         <SubNetworkRef type="int8">0</SubNetworkRef>
         <SceneTreeNodeRef type="int8">2</SceneTreeNodeRef>
         <AssetIndex type="int8">0</AssetIndex>
      </Association>
      <Association type="reference_string">
         3
         <NodeName type="string">Anchor|Castle_Whole1</NodeName>
         <Type type="string">CollisionShapeToCollisionInstance</Type>
         <CollisionInstanceRef type="int8">0</CollisionInstanceRef>
         <CollisionShapeRef type="int8">1</CollisionShapeRef>
      </Association>
      <Association type="reference_string">
         4
         <NodeName type="string">CellLink__REST_OF_WORLD_</NodeName>
         <Type type="string">CellLink</Type>
         <CellRef type="int8">0</CellRef>
         <LinkedCells type="int8_list"/>
         <LinkedSceneTreeNodeRefs type="int8_list">
            <entry>1</entry>
            <entry>2</entry>
         </LinkedSceneTreeNodeRefs>
      </Association>
      <Association type="reference_string">
         5
         <NodeName type="string">VisHierarchyLink_0</NodeName>
         <Type type="string">VisHierarchyLink</Type>
         <CellRef type="int8">0</CellRef>
         <LinkedNodeRefs type="int8_list">
            <entry>2</entry>
         </LinkedNodeRefs>
      </Association>
      <Association type="reference_string">
         6
         <NodeName type="string">Anchor</NodeName>
         <Type type="string">Transform</Type>
         <SceneTreeNodeRef type="int8">1</SceneTreeNodeRef>
         <SubNetworkRef type="int8">0</SubNetworkRef>
      </Association>
      <Association type="reference_string">
         7
         <NodeName type="string">Anchor</NodeName>
         <Type type="string">Anchor</Type>
         <SceneTreeNodeRef type="int8">1</SceneTreeNodeRef>
         <SubNetworkRef type="int8">0</SubNetworkRef>
      </Association>
      <Association type="reference_string">
         8
         <NodeName type="string">Anchor</NodeName>
         <Type type="string">PrimaryAnchor</Type>
         <SceneTreeNodeRef type="int8">1</SceneTreeNodeRef>
         <SubNetworkRef type="int8">0</SubNetworkRef>
      </Association>
      <Association type="reference_string">
         9
         <NodeName type="string">Anchor|Castle_Whole1</NodeName>
         <Type type="string">Geometry</Type>
         <SceneTreeNodeRef type="int8">2</SceneTreeNodeRef>
         <SubNetworkRef type="int8">0</SubNetworkRef>
      </Association>
   </AssociationPool>
   <ExporterDate type="string">Jun  3 2015</ExporterDate>
   <ExporterTime type="string">17:59:11</ExporterTime>
</root_node>
'''

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