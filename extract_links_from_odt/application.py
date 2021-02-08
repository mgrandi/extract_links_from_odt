import logging
import pathlib

from odf.opendocument import load
import odf.text

from extract_links_from_odt import constants

logger = logging.getLogger()


class Application:

    def __init__(self, args):

        self.args = args

    def run(self):

        output_file = self.args.output_file
        input_file = self.args.odt_file


        logger.info("opening file: `%s`", input_file)
        odt_file = load(str(input_file))

        # the A elements seems to be the ones we want
        # from `content.xml`
        # <text:a
        #   xlink:type="simple"
        #   xlink:href="https://example.com"
        #   text:style-name="ListLabel_20_506"
        #   text:visited-style-name="ListLabel_20_506">example text</text:span></text:a>
        list_of_link_elements = odt_file.getElementsByType(odf.text.A)

        logger.info("found `%s` links:", len(list_of_link_elements))

        with open(output_file, "w", encoding="utf-8") as f:

            for iter_link_element in list_of_link_elements:

                iter_link = iter_link_element.attributes[constants.ATTRIBUTE_DICT_KEY_HREF]

                f.write(f"{iter_link}\n")