<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>Population_Density_Classes</sld:Name>            
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name/>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>grid</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:Opacity>1</sld:Opacity>
                        <sld:ColorMap>
                            <sld:ColorMapEntry color="#ffffff" label="0 - 60" opacity="1.0" quantity="1"/>
                            <sld:ColorMapEntry color="#79ad00" label="61 - 160" opacity="1.0" quantity="4.5"/>
                            <sld:ColorMapEntry color="#fffc06" label="161 - 300" opacity="1.0" quantity="8"/>
                            <sld:ColorMapEntry color="#ff9900" label="301 - 400" opacity="1.0" quantity="11.5"/>
                            <sld:ColorMapEntry color="#fb2402" label="401 - 3360" opacity="1.0" quantity="15"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>