<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>Drainage_Density_2018</sld:Name>            
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
                            <sld:ColorMapEntry color="#ffffff" label="Nil" opacity="1.0" quantity="0"/>
                            <sld:ColorMapEntry color="#feffdf" label="Less (0.01 -1)" opacity="1.0" quantity="1"/>
                            <sld:ColorMapEntry color="#fcd681" label="Moderate (1.1 - 2)" opacity="1.0" quantity="2"/>
                            <sld:ColorMapEntry color="#f66211" label="High (2.1 - 2.5)" opacity="1.0" quantity="2.5"/>
                            <sld:ColorMapEntry color="#71120b" label="Very High (2.6 - 3.3)" opacity="1.0" quantity="3.3"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>