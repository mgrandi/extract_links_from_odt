import attr
import odf.element

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class OpenDocumentTextLink:
    url:str = attr.ib()
    link_text:str = attr.ib()
    odf_element:odf.element.Element = attr.ib()