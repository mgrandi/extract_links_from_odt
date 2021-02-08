import logging
import pathlib

from odf.opendocument import load
import odf.text

from extract_links_from_odt import constants
from extract_links_from_odt import model

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
        list_of_odt_link_objs = []

        for iter_link_element in odt_file.getElementsByType(odf.text.A):

            iter_odt_link = model.OpenDocumentTextLink(
                url=iter_link_element.attributes[constants.ATTRIBUTE_DICT_KEY_HREF],
                link_text=str(iter_link_element), # why is it so hard to get the text of a element here lol
                odf_element=iter_link_element)

            list_of_odt_link_objs.append(iter_odt_link)

        logger.info("found `%s` links", len(list_of_odt_link_objs))


        matched = 0
        nomatch = 0
        with open(output_file, "w", encoding="utf-8") as f:

            for idx, iter_odt_link_obj in enumerate(list_of_odt_link_objs):

                logger.debug("on item: `%s`", iter_odt_link_obj)


                if self.args.filter:

                    match_obj = self.args.filter.search(iter_odt_link_obj.url)

                    logger.debug("testing link `%s` against the regex `%s`: result is `%s`", iter_odt_link_obj.url, self.args.filter, match_obj)

                    if match_obj:

                        if idx != 0:
                            f.write("\n")
                        f.write(f"{iter_odt_link_obj.url}")
                        matched += 1

                    else:
                        logger.debug("not writing link `%s`, didn't match the regex", iter_odt_link_obj.url)
                        nomatch += 1
                        continue

                else:

                    logger.debug("writing link `%s`, no regex was passed in to validate against", iter_odt_link_obj.url)

                    if idx != 0:
                        f.write("\n")
                    f.write(f"{iter_odt_link_obj.url}")
                    match += 1

        logger.info("`%s` urls matched, `%s` urls didn't match", matched, nomatch)