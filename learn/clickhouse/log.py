import logging as _logging

_logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=_logging.INFO)
_logging.info("test")
print("ad")