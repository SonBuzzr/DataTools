<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>Grownd_Water_Potential_Zone</sld:Name>            
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name/>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>grid</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:Opacity>1</sld:Opacity>
                        <sld:ColorMap type="intervals">
                            <sld:ColorMapEntry color="#f5aeb4" label="0 - 0.2" opacity="1.0" quantity="0.2"/>
                            <sld:ColorMapEntry color="#ffda5b" label="0.2 - 0.4" opacity="1.0" quantity="0.4"/>
                            <sld:ColorMapEntry color="#cdffad" label="0.4 - 0.6" opacity="1.0" quantity="0.6"/>
                            <sld:ColorMapEntry color="#74cef7" label="0.6 - 0.8" opacity="1.0" quantity="0.8"/>
                            <sld:ColorMapEntry color="#4d4dff" label="0.8 - 1" opacity="1.0" quantity="1"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>