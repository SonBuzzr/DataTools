<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>DEM</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry quantity="0" label="0"  color="#ffffcc"/>
              <sld:ColorMapEntry quantity="500" label="500" color="#d0edc0"/>
              <sld:ColorMapEntry quantity="1500" label="1500" color="#a1dab4"/>
              <sld:ColorMapEntry quantity="2500" label="2500" color="#71c8bc"/>
              <sld:ColorMapEntry quantity="3500" label="3500" color="#41b6c4"/>
              <sld:ColorMapEntry quantity="4500" label="4500" color="#369bbe"/>
              <sld:ColorMapEntry quantity="5500" label="5500" color="#2c7fb8"/>
              <sld:ColorMapEntry quantity="6500" label="6500" color="#2859a6"/>
              <sld:ColorMapEntry quantity="7500" label="7500" color="#253494"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>