<xsl:stylesheet 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:fo="http://www.w3.org/1999/XSL/Format"
    version="1.1"
>
    <!-- $Date: 2011-01-09 02:51:33 -0500 (Sun, 09 Jan 2011) $ -->

    <xsl:include href = "parameters.xsl"/>
    <xsl:include href="body_elements.xsl"/>
    <xsl:include href="page.xsl"/>
    <xsl:include href = "header_footer.xsl"/>
    <xsl:include href = "root.xsl"/>




    <xsl:output method="xml" encoding="UTF-8"/>

    <xsl:template match="/">
        <xsl:element name="fo:root">
            <xsl:call-template name="make-pages">
                <xsl:with-param name="page-layout" select="$page-layout"/>
            </xsl:call-template>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>


    <xsl:template match="*">
        <xsl:message>
            <xsl:text>no match for </xsl:text>
            <xsl:value-of select="name(.)"/>
        </xsl:message>
    </xsl:template>


</xsl:stylesheet>
