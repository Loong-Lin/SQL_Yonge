
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDnonassocLELEGEGTEQNEADD ALL ALTER AND ASC CHAR CREATE CREATEINDEX CREATETABLE CREATEUSER DELETE DESC DROP DROPINDEX DROPTABLE EQ EXIT FROM GE GRANT GT HELP ID INDEX INSERT INT INTO IS KEY LE LOAD LT NE NOT NULL NUMBER ON OR PASSWORD PRIMARY PRINT REVOKE SELECT SET SHOW STRING TABLE TABLES TO UPDATE USER VALUES VIEW WHERE start : command ';'  command : ddl\n                | dml\n                | utility\n                | nothing  ddl : createtable\n            | createindex\n            | droptable\n            | dropindex\n            | showtables\n            | altertable\n            | createuser\n            | grantuser\n            | revokeuser  dml : query\n            | insert\n            | delete\n            | update  utility : exit\n                | print\n                | desc  showtables : SHOW TABLES  createuser : CREATE USER ID PASSWORD STRING grantuser : GRANT power_list ON non_mrelation_list TO non_mrelation_list  revokeuser : REVOKE power_list ON non_mrelation_list FROM non_mrelation_list  power_list : power_list ',' power_type\n                   | power_type   power_type : SELECT\n                    | UPDATE\n                    | INSERT\n                    | DELETE\n                    | PRINT\n                    | ALTER\n                    | CREATETABLE\n                    | CREATEUSER\n                    | DROPTABLE\n                    | DROPINDEX\n                    | CREATEINDEX\n                    | ALL\n                    | DESC\n     altertable : ALTER TABLE ID ADD attrtype\n                   | ALTER TABLE ID DROP non_mrelation_list  createtable : CREATE TABLE ID '(' non_mattrtype_list ')'  createindex : CREATE INDEX ID '(' ID ')'  droptable : DROP TABLE ID  dropindex : DROP INDEX ID '(' ID ')'  print : PRINT ID desc : DESC ID  exit : EXIT  query : SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause  insert : INSERT INTO ID VALUES inservalue_list  inservalue_list : '(' non_mvalue_list ')' ',' inservalue_list\n                        | '(' non_mvalue_list ')'  delete : DELETE FROM ID opwhere_clause  update : UPDATE ID SET relattr EQ relattr_or_value opwhere_clause  non_mattrtype_list : attrtype ',' non_mattrtype_list\n                           | attrtype  attrtype : ID type\n                 | ID type '(' NUMBER ')'\n                 | PRIMARY KEY '(' ID ')'  type : INT\n             | CHAR  non_mselect_clause : non_mrelattr_list\n                           | '*'  non_mrelattr_list : relattr ',' non_mrelattr_list\n                          | relattr  relattr : ID '.' ID\n                | ID  non_mrelation_list : relation ',' non_mrelation_list\n                           | relation  relation : ID  opwhere_clause : WHERE non_mcond_list\n                       | nothing  non_mcond_list : non_mcond_list AND non_mcond_list\n                       | non_mcond_list OR  non_mcond_list\n                       | '(' non_mcond_list ')'\n                       | condition  condition : relattr op relattr_or_value\n                  | relattr EQ null_value\n                  | relattr NE null_value  relattr_or_value : relattr\n                         | value  non_mvalue_list : value ',' non_mvalue_list\n                        | value\n                        | null_value ',' non_mvalue_list\n                        | null_value  value : STRING  value : NUMBER  null_value : NULL  op : LT\n           | LE\n           | GT\n           | GE\n           | EQ\n           | NE  nothing : "
    
_lr_action_items = {';':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,33,42,64,68,69,73,83,92,93,96,98,100,102,109,111,112,116,117,119,121,124,125,126,127,130,131,132,133,134,138,139,140,151,152,153,157,160,161,162,163,164,165,166,172,173,174,],[-96,36,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-49,-22,-68,-47,-48,-45,-96,-70,-71,-96,-67,-54,-73,-23,-41,-42,-50,-51,-72,-77,-58,-61,-62,-43,-44,-46,-24,-69,-25,-87,-88,-89,-81,-96,-82,-53,-74,-75,-76,-78,-79,-80,-55,-59,-60,-52,]),'CREATE':([0,],[23,]),'DROP':([0,75,],[24,90,]),'SHOW':([0,],[25,]),'ALTER':([0,27,28,77,],[26,51,51,51,]),'GRANT':([0,],[27,]),'REVOKE':([0,],[28,]),'SELECT':([0,27,28,77,],[29,46,46,46,]),'INSERT':([0,27,28,77,],[30,48,48,48,]),'DELETE':([0,27,28,77,],[31,49,49,49,]),'UPDATE':([0,27,28,77,],[32,47,47,47,]),'EXIT':([0,],[33,]),'PRINT':([0,27,28,77,],[34,50,50,50,]),'DESC':([0,27,28,77,],[35,58,58,58,]),'$end':([1,36,],[0,-1,]),'TABLE':([23,24,26,],[37,40,43,]),'INDEX':([23,24,],[38,41,]),'USER':([23,],[39,]),'TABLES':([25,],[42,]),'CREATETABLE':([27,28,77,],[52,52,52,]),'CREATEUSER':([27,28,77,],[53,53,53,]),'DROPTABLE':([27,28,77,],[54,54,54,]),'DROPINDEX':([27,28,77,],[55,55,55,]),'CREATEINDEX':([27,28,77,],[56,56,56,]),'ALL':([27,28,77,],[57,57,57,]),'*':([29,],[62,]),'ID':([29,32,34,35,37,38,39,40,41,43,65,66,76,78,79,80,81,84,85,86,88,89,90,101,113,114,115,120,123,128,141,142,144,145,146,147,148,149,150,156,],[64,67,68,69,70,71,72,73,74,75,82,83,93,93,93,64,98,64,104,108,110,104,93,64,93,93,93,64,64,104,64,64,64,-94,-95,-90,-91,-92,-93,168,]),'INTO':([30,],[65,]),'FROM':([31,60,61,62,63,64,92,93,95,97,98,133,],[66,79,-63,-64,-66,-68,-70,-71,115,-65,-67,-69,]),'ON':([44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,94,],[76,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,78,-26,]),',':([44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,92,93,94,98,106,124,125,126,136,137,138,139,140,157,172,173,],[77,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,77,80,-68,114,-71,-26,-67,128,-58,-61,-62,158,159,-87,-88,-89,169,-59,-60,]),'.':([64,],[81,]),'EQ':([64,98,103,122,],[-68,-67,123,145,]),'NE':([64,98,122,],[-68,-67,146,]),'LT':([64,98,122,],[-68,-67,147,]),'LE':([64,98,122,],[-68,-67,148,]),'GT':([64,98,122,],[-68,-67,149,]),'GE':([64,98,122,],[-68,-67,150,]),'WHERE':([64,83,92,93,96,98,133,138,139,151,152,153,],[-68,101,-70,-71,101,-67,-69,-87,-88,-81,101,-82,]),'AND':([64,98,119,121,138,139,140,143,151,153,160,161,162,163,164,165,],[-68,-67,141,-77,-87,-88,-89,141,-81,-82,-74,141,-76,-78,-79,-80,]),'OR':([64,98,119,121,138,139,140,143,151,153,160,161,162,163,164,165,],[-68,-67,142,-77,-87,-88,-89,142,-81,-82,-74,-75,-76,-78,-79,-80,]),')':([64,98,105,106,108,110,121,124,125,126,135,136,137,138,139,140,143,151,153,155,160,161,162,163,164,165,167,168,170,171,172,173,],[-68,-67,127,-57,130,131,-77,-58,-61,-62,157,-84,-86,-87,-88,-89,162,-81,-82,-56,-74,-75,-76,-78,-79,-80,172,173,-83,-85,-59,-60,]),'SET':([67,],[84,]),'(':([70,71,74,99,101,120,124,125,126,129,141,142,169,],[85,86,88,118,120,120,154,-61,-62,156,120,120,118,]),'PASSWORD':([72,],[87,]),'ADD':([75,],[89,]),'VALUES':([82,],[99,]),'PRIMARY':([85,89,128,],[107,107,107,]),'STRING':([87,118,123,144,145,146,147,148,149,150,158,159,],[109,138,138,138,-94,-95,-90,-91,-92,-93,138,138,]),'TO':([91,92,93,133,],[113,-70,-71,-69,]),'INT':([104,],[125,]),'CHAR':([104,],[126,]),'KEY':([107,],[129,]),'NUMBER':([118,123,144,145,146,147,148,149,150,154,158,159,],[139,139,139,-94,-95,-90,-91,-92,-93,167,139,139,]),'NULL':([118,145,146,158,159,],[140,140,140,140,140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'command':([0,],[2,]),'ddl':([0,],[3,]),'dml':([0,],[4,]),'utility':([0,],[5,]),'nothing':([0,83,96,152,],[6,102,102,102,]),'createtable':([0,],[7,]),'createindex':([0,],[8,]),'droptable':([0,],[9,]),'dropindex':([0,],[10,]),'showtables':([0,],[11,]),'altertable':([0,],[12,]),'createuser':([0,],[13,]),'grantuser':([0,],[14,]),'revokeuser':([0,],[15,]),'query':([0,],[16,]),'insert':([0,],[17,]),'delete':([0,],[18,]),'update':([0,],[19,]),'exit':([0,],[20,]),'print':([0,],[21,]),'desc':([0,],[22,]),'power_list':([27,28,],[44,59,]),'power_type':([27,28,77,],[45,45,94,]),'non_mselect_clause':([29,],[60,]),'non_mrelattr_list':([29,80,],[61,97,]),'relattr':([29,80,84,101,120,123,141,142,144,],[63,63,103,122,122,151,122,122,151,]),'non_mrelation_list':([76,78,79,90,113,114,115,],[91,95,96,112,132,133,134,]),'relation':([76,78,79,90,113,114,115,],[92,92,92,92,92,92,92,]),'opwhere_clause':([83,96,152,],[100,116,166,]),'non_mattrtype_list':([85,128,],[105,155,]),'attrtype':([85,89,128,],[106,111,106,]),'inservalue_list':([99,169,],[117,174,]),'non_mcond_list':([101,120,141,142,],[119,143,160,161,]),'condition':([101,120,141,142,],[121,121,121,121,]),'type':([104,],[124,]),'non_mvalue_list':([118,158,159,],[135,170,171,]),'value':([118,123,144,158,159,],[136,153,153,136,136,]),'null_value':([118,145,146,158,159,],[137,164,165,137,137,]),'op':([122,],[144,]),'relattr_or_value':([123,144,],[152,163,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> command ;','start',2,'p_start','parser.py',22),
  ('command -> ddl','command',1,'p_command','parser.py',27),
  ('command -> dml','command',1,'p_command','parser.py',28),
  ('command -> utility','command',1,'p_command','parser.py',29),
  ('command -> nothing','command',1,'p_command','parser.py',30),
  ('ddl -> createtable','ddl',1,'p_ddl','parser.py',35),
  ('ddl -> createindex','ddl',1,'p_ddl','parser.py',36),
  ('ddl -> droptable','ddl',1,'p_ddl','parser.py',37),
  ('ddl -> dropindex','ddl',1,'p_ddl','parser.py',38),
  ('ddl -> showtables','ddl',1,'p_ddl','parser.py',39),
  ('ddl -> altertable','ddl',1,'p_ddl','parser.py',40),
  ('ddl -> createuser','ddl',1,'p_ddl','parser.py',41),
  ('ddl -> grantuser','ddl',1,'p_ddl','parser.py',42),
  ('ddl -> revokeuser','ddl',1,'p_ddl','parser.py',43),
  ('dml -> query','dml',1,'p_dml','parser.py',48),
  ('dml -> insert','dml',1,'p_dml','parser.py',49),
  ('dml -> delete','dml',1,'p_dml','parser.py',50),
  ('dml -> update','dml',1,'p_dml','parser.py',51),
  ('utility -> exit','utility',1,'p_utility','parser.py',56),
  ('utility -> print','utility',1,'p_utility','parser.py',57),
  ('utility -> desc','utility',1,'p_utility','parser.py',58),
  ('showtables -> SHOW TABLES','showtables',2,'p_showtables','parser.py',64),
  ('createuser -> CREATE USER ID PASSWORD STRING','createuser',5,'p_createuser','parser.py',70),
  ('grantuser -> GRANT power_list ON non_mrelation_list TO non_mrelation_list','grantuser',6,'p_grantuser','parser.py',76),
  ('revokeuser -> REVOKE power_list ON non_mrelation_list FROM non_mrelation_list','revokeuser',6,'p_revokeuser','parser.py',82),
  ('power_list -> power_list , power_type','power_list',3,'p_power_list','parser.py',87),
  ('power_list -> power_type','power_list',1,'p_power_list','parser.py',88),
  ('power_type -> SELECT','power_type',1,'p_power_type','parser.py',96),
  ('power_type -> UPDATE','power_type',1,'p_power_type','parser.py',97),
  ('power_type -> INSERT','power_type',1,'p_power_type','parser.py',98),
  ('power_type -> DELETE','power_type',1,'p_power_type','parser.py',99),
  ('power_type -> PRINT','power_type',1,'p_power_type','parser.py',100),
  ('power_type -> ALTER','power_type',1,'p_power_type','parser.py',101),
  ('power_type -> CREATETABLE','power_type',1,'p_power_type','parser.py',102),
  ('power_type -> CREATEUSER','power_type',1,'p_power_type','parser.py',103),
  ('power_type -> DROPTABLE','power_type',1,'p_power_type','parser.py',104),
  ('power_type -> DROPINDEX','power_type',1,'p_power_type','parser.py',105),
  ('power_type -> CREATEINDEX','power_type',1,'p_power_type','parser.py',106),
  ('power_type -> ALL','power_type',1,'p_power_type','parser.py',107),
  ('power_type -> DESC','power_type',1,'p_power_type','parser.py',108),
  ('altertable -> ALTER TABLE ID ADD attrtype','altertable',5,'p_altertable','parser.py',116),
  ('altertable -> ALTER TABLE ID DROP non_mrelation_list','altertable',5,'p_altertable','parser.py',117),
  ('createtable -> CREATE TABLE ID ( non_mattrtype_list )','createtable',6,'p_createtable','parser.py',127),
  ('createindex -> CREATE INDEX ID ( ID )','createindex',6,'p_createindex','parser.py',133),
  ('droptable -> DROP TABLE ID','droptable',3,'p_droptable','parser.py',139),
  ('dropindex -> DROP INDEX ID ( ID )','dropindex',6,'p_dropindex','parser.py',145),
  ('print -> PRINT ID','print',2,'p_print','parser.py',151),
  ('desc -> DESC ID','desc',2,'p_desc','parser.py',157),
  ('exit -> EXIT','exit',1,'p_exit','parser.py',162),
  ('query -> SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause','query',5,'p_query','parser.py',168),
  ('insert -> INSERT INTO ID VALUES inservalue_list','insert',5,'p_insert','parser.py',174),
  ('inservalue_list -> ( non_mvalue_list ) , inservalue_list','inservalue_list',5,'p_inservalue_list','parser.py',180),
  ('inservalue_list -> ( non_mvalue_list )','inservalue_list',3,'p_inservalue_list','parser.py',181),
  ('delete -> DELETE FROM ID opwhere_clause','delete',4,'p_delete','parser.py',190),
  ('update -> UPDATE ID SET relattr EQ relattr_or_value opwhere_clause','update',7,'p_update','parser.py',196),
  ('non_mattrtype_list -> attrtype , non_mattrtype_list','non_mattrtype_list',3,'p_non_mattrtype_list','parser.py',201),
  ('non_mattrtype_list -> attrtype','non_mattrtype_list',1,'p_non_mattrtype_list','parser.py',202),
  ('attrtype -> ID type','attrtype',2,'p_attrtype','parser.py',210),
  ('attrtype -> ID type ( NUMBER )','attrtype',5,'p_attrtype','parser.py',211),
  ('attrtype -> PRIMARY KEY ( ID )','attrtype',5,'p_attrtype','parser.py',212),
  ('type -> INT','type',1,'p_type','parser.py',222),
  ('type -> CHAR','type',1,'p_type','parser.py',223),
  ('non_mselect_clause -> non_mrelattr_list','non_mselect_clause',1,'p_non_mselect_clause','parser.py',229),
  ('non_mselect_clause -> *','non_mselect_clause',1,'p_non_mselect_clause','parser.py',230),
  ('non_mrelattr_list -> relattr , non_mrelattr_list','non_mrelattr_list',3,'p_non_mrelattr_list','parser.py',235),
  ('non_mrelattr_list -> relattr','non_mrelattr_list',1,'p_non_mrelattr_list','parser.py',236),
  ('relattr -> ID . ID','relattr',3,'p_relattr','parser.py',244),
  ('relattr -> ID','relattr',1,'p_relattr','parser.py',245),
  ('non_mrelation_list -> relation , non_mrelation_list','non_mrelation_list',3,'p_non_mrelation_list','parser.py',253),
  ('non_mrelation_list -> relation','non_mrelation_list',1,'p_non_mrelation_list','parser.py',254),
  ('relation -> ID','relation',1,'p_relation','parser.py',262),
  ('opwhere_clause -> WHERE non_mcond_list','opwhere_clause',2,'p_opwhere_clause','parser.py',267),
  ('opwhere_clause -> nothing','opwhere_clause',1,'p_opwhere_clause','parser.py',268),
  ('non_mcond_list -> non_mcond_list AND non_mcond_list','non_mcond_list',3,'p_non_mcond_list','parser.py',274),
  ('non_mcond_list -> non_mcond_list OR non_mcond_list','non_mcond_list',3,'p_non_mcond_list','parser.py',275),
  ('non_mcond_list -> ( non_mcond_list )','non_mcond_list',3,'p_non_mcond_list','parser.py',276),
  ('non_mcond_list -> condition','non_mcond_list',1,'p_non_mcond_list','parser.py',277),
  ('condition -> relattr op relattr_or_value','condition',3,'p_condition','parser.py',287),
  ('condition -> relattr EQ null_value','condition',3,'p_condition','parser.py',288),
  ('condition -> relattr NE null_value','condition',3,'p_condition','parser.py',289),
  ('relattr_or_value -> relattr','relattr_or_value',1,'p_relattr_or_value','parser.py',294),
  ('relattr_or_value -> value','relattr_or_value',1,'p_relattr_or_value','parser.py',295),
  ('non_mvalue_list -> value , non_mvalue_list','non_mvalue_list',3,'p_non_mvalue_list','parser.py',300),
  ('non_mvalue_list -> value','non_mvalue_list',1,'p_non_mvalue_list','parser.py',301),
  ('non_mvalue_list -> null_value , non_mvalue_list','non_mvalue_list',3,'p_non_mvalue_list','parser.py',302),
  ('non_mvalue_list -> null_value','non_mvalue_list',1,'p_non_mvalue_list','parser.py',303),
  ('value -> STRING','value',1,'p_value_string','parser.py',311),
  ('value -> NUMBER','value',1,'p_value_number','parser.py',316),
  ('null_value -> NULL','null_value',1,'p_null_value','parser.py',321),
  ('op -> LT','op',1,'p_op','parser.py',327),
  ('op -> LE','op',1,'p_op','parser.py',328),
  ('op -> GT','op',1,'p_op','parser.py',329),
  ('op -> GE','op',1,'p_op','parser.py',330),
  ('op -> EQ','op',1,'p_op','parser.py',331),
  ('op -> NE','op',1,'p_op','parser.py',332),
  ('nothing -> <empty>','nothing',0,'p_nothing','parser.py',337),
]
