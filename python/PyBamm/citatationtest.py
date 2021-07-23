import pybtex

citations = pybtex.format_from_file(
                "./test.bib",
                "plain"
            )
print(citations)