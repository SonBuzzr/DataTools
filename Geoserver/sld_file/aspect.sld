<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:gml="http://www.opengis.net/gml" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>aspect_reclass</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="values">
              <sld:ColorMapEntry color="#6ee16e" label="Flat" quantity="1"/>
              <sld:ColorMapEntry color="#dc0f0f" label="North" quantity="2"/>
              <sld:ColorMapEntry color="#44cea0" label="Northeast" quantity="3"/>
              <sld:ColorMapEntry color="#3fb1ea" label="East" quantity="4"/>
              <sld:ColorMapEntry color="#de9a13" label="Southeast" quantity="5"/>
              <sld:ColorMapEntry color="#6464ef" label="South" quantity="6"/>
              <sld:ColorMapEntry color="#e633ab" label="Southwest" quantity="7"/>
              <sld:ColorMapEntry color="#b9ef4d" label="West" quantity="8"/>
              <sld:ColorMapEntry color="#9e45ca" label="Northwest" quantity="9"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>