# # -*- coding: UTF-8 -*-
# # @Anthor : alexuh
# # @Email : alexuh@zamplus.com
# # @Created: 2019-08-16
# from xray import db as _db
# from xray.uri import URI as _URI
# import ConfigParser as _ConfigParser
# import xray as _xray
# import os as _os
#
# _conf_parser = _ConfigParser.ConfigParser()
# _conf_parser.read([_os.path.join(_os.path.dirname(__file__), "default.conf"), _os.path.join(_xray.CONF_DIR, "ciimc-common.conf")])
# DB_URL = str(_URI(_conf_parser.get("ciimc-common", "db-url")))
#
#
# def schema_generate(h=None, message_class=None):
#     import xlwt
#     workbook = xlwt.Workbook(encoding='utf-8')
#     sheet = workbook.add_sheet(message_class)
#     init_db_client = h is None
#     if init_db_client:
#         h = _db.open(DB_URL)
#     global sql
#     type = []
#     list = ["int"]
#     data = [["message_class", "message_type", "name", "display_name", "data_type", "description"]]
#     try:
#         if message_class == "status":
#             sql_type = "SELECT message_type FROM generic_property_binding WHERE message_class='status' and message_type!= '*' GROUP BY message_type"
#             for row in h.execute(sql_type):
#                 type.append(row[0])
#             sql = "SELECT message_class, gb.message_type, gb.`name`, g.display_name, data_type, description,m.display_name type1 FROM ( generic_property_binding gb LEFT JOIN generic_property g ON gb.NAME = g.NAME ) LEFT JOIN message_type_value m ON gb.message_type = m.`code` WHERE message_class='%s'" % message_class
#         else:
#             sql = "SELECT message_class, gb.message_type, gb.`name`, g.display_name, data_type, description FROM generic_property_binding gb LEFT JOIN generic_property g ON gb.NAME = g.NAME WHERE message_class = '%s'" % message_class
#         for row in h.execute(sql):
#             message_class = row[0]
#             message_type = row[1]
#             name = row[2]
#             display_name = row[3]
#             data_type = row[4]
#             description = row[5]
#             if len(row) == 7:
#                 if row[6] is not None:
#                     message_type = message_type + "-" + row[6]
#             if message_class == "status" and message_type == "*":
#                 message_type = ",".join(type)
#             if data_type == "boolean":
#                 data_type = "int"
#             elif data_type == "string":
#                 data_type = "varchar(255)"
#             elif data_type not in list:
#                 data_type = "MediumText"
#             elif data_type == "timestamp":
#                 data_type = "bigint"
#             elif data_type == "float":
#                 data_type = "double(255, 20)"
#             data.append([message_class, message_type, name, display_name, data_type, description])
#             _xray.logger.info("message_class: %s, message_type: %s, name: %s, display_name: %s, data_type: %s description: %s" % (message_class, message_type, name, display_name, data_type, description))
#         line = 0
#         for i in data:
#             sheet.write(line, 0, i[0])
#             sheet.write(line, 1, i[1])
#             sheet.write(line, 2, i[2])
#             sheet.write(line, 3, i[3])
#             sheet.write(line, 4, i[4])
#             sheet.write(line, 5, i[5])
#             line += 1
#         workbook.save("/tmp/%s.xlsx" % message_class)
#     finally:
#         if init_db_client:
#             del h
#
