
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'fileleftLORleftLANDleftORleftXORleftANDleftEQNEleftGTGELTLEleftRSHIFTLSHIFTleftPLUSMINUSleftTIMESDIVIDEMODID STRING MULTI_STRING INT FLOAT PLUS MINUS TIMES DIVIDE MOD OR AND XOR LSHIFT RSHIFT LOR LAND LNOT LT LE GT GE EQ NE EQUALS LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE COMMA SEMI COLON WRITE NOP RETURN READD FOR FALSE ELSE TRUE DEF IFfile : functions\n                | bodyfunctions : function\n                     | functions functionfuncall : ID LPAREN funcall_params RPARENfuncall_params : empty\n                          | expression\n                          | funcall_params COMMA expressionfunction : DEF ID LPAREN fun_params RPAREN LBRACE body RBRACEfun_params : empty\n                      | ID\n                      | fun_pointer\n                      | fun_params COMMA fun_pointer\n                      | fun_params COMMA IDfun_pointer : ID LPAREN RPARENbody : ex\n                | body exex : assign SEMI\n              | return SEMI\n              | write SEMI\n              | readd SEMI\n              | funcall SEMI\n              | readd_esc SEMI\n              | nop SEMI\n              | if\n              | foreach\n              | readd_escnop : NOPif : IF LPAREN expression RPAREN LBRACE body RBRACE\n              | IF LPAREN expression RPAREN LBRACE body RBRACE ELSE if\n              | IF LPAREN expression RPAREN LBRACE body RBRACE ELSE LBRACE body RBRACEforeach : FOR LPAREN var COLON value RPAREN LBRACE body RBRACEreturn : RETURN expressionwrite : WRITE expressionreadd : READD expressionreadd_esc :  LT string GTreadd_esc :  LT ID string GTassign : var EQUALS expressionexpression : value\n                      | bool_ex\n                      | op_exbool_ex : bool_value EQ bool_value\n                   | bool_value NE bool_value\n                   | bool_value LE bool_value\n                   | bool_value GE bool_value\n                   | bool_value LT bool_value\n                   | bool_value GT bool_value\n                   | bool_value LOR bool_value\n                   | bool_value LAND bool_valuebool_ex : LNOT bool_value\n                   | LPAREN bool_ex RPARENbool_value : value\n                                  | op_exop_ex : value PLUS value\n                 | value MINUS value\n                 | value TIMES value\n                 | value DIVIDE value\n                 | value MOD value\n                 | value LSHIFT value\n                 | value RSHIFT value\n                 | value OR value\n                 | value AND value\n                 | value XOR value\n\n                 | value PLUS op_ex\n                 | value MINUS op_ex\n                 | value TIMES op_ex\n                 | value DIVIDE op_ex\n                 | value MOD op_ex\n                 | value LSHIFT op_ex\n                 | value RSHIFT op_ex\n                 | value OR op_ex\n                 | value AND op_ex\n                 | value XOR op_exop_ex : LPAREN op_ex RPARENvalue : var\n                 | int\n                 | float\n                 | string\n                 | bool\n                 | funcall\n                 | list\n                 | array_get\n                 | tree_getint : INTfloat : FLOATstring : STRINGstring : MULTI_STRINGbool : TRUEbool : FALSElist : LBRACKET array RBRACKETarray : value\n                 | array COMMA valuearray_get : ID LBRACKET INT RBRACKETtree_get : ID LBRACKET string RBRACKETvar : IDempty :'
    
_lr_action_items = {'DIVIDE':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,86,86,86,86,86,86,86,86,86,86,86,86,86,86,-90,-5,-93,-94,]),'LNOT':([2,18,22,39,56,63,64,148,],[25,25,25,25,25,25,25,25,]),'RETURN':([0,5,8,12,14,15,49,50,55,57,58,59,62,66,97,145,158,159,164,165,166,167,169,171,172,173,174,175,],[2,-16,-25,-26,-27,2,-21,-22,-20,-23,-17,-19,-24,-18,-36,-37,2,2,2,2,2,-29,2,-32,2,-30,2,-31,]),'LBRACKET':([2,18,22,25,39,40,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[47,47,47,47,47,82,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'COLON':([99,100,],[146,-95,]),'LSHIFT':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,89,89,89,89,89,89,89,89,89,89,89,89,89,89,-90,-5,-93,-94,]),'RSHIFT':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,85,85,85,85,85,85,85,85,85,85,85,85,85,85,-90,-5,-93,-94,]),'TRUE':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'MINUS':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,91,91,91,91,91,91,91,91,91,91,91,91,91,91,-90,-5,-93,-94,]),'DEF':([0,1,9,52,168,],[7,-3,7,-4,-9,]),'STRING':([2,10,18,22,25,39,47,53,56,63,64,69,71,72,73,74,75,76,77,78,82,83,84,85,86,87,88,89,90,91,92,139,146,148,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'LE':([26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,80,81,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,147,150,151,],[-76,-77,-88,-83,-87,-53,71,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,-53,-52,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-5,-93,-94,]),'RPAREN':([26,27,28,29,30,31,32,34,35,36,37,38,40,41,42,43,44,45,46,63,67,68,70,79,80,95,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,147,150,151,155,156,157,160,161,162,],[-76,-77,-88,-83,-40,-87,-41,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-39,-96,-53,-50,-52,115,116,-96,-6,147,-7,149,116,-44,-43,-46,-48,-45,-47,-49,-42,-51,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-12,153,-10,-11,-5,-93,-94,162,163,-8,-13,-14,-15,]),'SEMI':([3,4,11,14,16,19,23,24,26,27,28,29,30,31,32,34,35,36,37,38,40,41,42,43,44,45,46,48,61,65,67,68,70,97,98,107,108,109,110,111,112,113,114,115,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,145,147,150,151,],[49,50,55,57,59,62,-28,66,-76,-77,-88,-83,-40,-87,-41,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-39,-33,-34,-35,-53,-50,-52,-36,-38,-44,-43,-46,-48,-45,-47,-49,-42,-51,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-37,-5,-93,-94,]),'MULTI_STRING':([2,10,18,22,25,39,47,53,56,63,64,69,71,72,73,74,75,76,77,78,82,83,84,85,86,87,88,89,90,91,92,139,146,148,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'NE':([26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,80,81,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,147,150,151,],[-76,-77,-88,-83,-87,-53,72,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,-53,-52,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-5,-93,-94,]),'LT':([0,5,8,12,14,15,26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,49,50,55,57,58,59,62,66,80,81,97,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,145,147,150,151,158,159,164,165,166,167,169,171,172,173,174,175,],[10,-16,-25,-26,-27,10,-76,-77,-88,-83,-87,-53,73,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,-21,-22,-20,-23,-17,-19,-24,-18,-53,-52,-36,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-37,-5,-93,-94,10,10,10,10,10,-29,10,-32,10,-30,10,-31,]),'PLUS':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,88,88,88,88,88,88,88,88,88,88,88,88,88,88,-90,-5,-93,-94,]),'COMMA':([26,27,28,29,30,31,32,34,35,36,37,38,40,41,42,43,44,45,46,63,67,68,70,93,94,95,101,102,103,107,108,109,110,111,112,113,114,115,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,147,150,151,152,157,160,161,162,],[-76,-77,-88,-83,-40,-87,-41,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-39,-96,-53,-50,-52,139,-91,-96,-6,148,-7,-44,-43,-46,-48,-45,-47,-49,-42,-51,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-12,154,-10,-11,-5,-93,-94,-92,-8,-13,-14,-15,]),'$end':([1,5,6,8,9,12,14,15,49,50,52,55,57,58,59,62,66,97,145,167,168,171,173,175,],[-3,-16,0,-25,-1,-26,-27,-2,-21,-22,-4,-20,-23,-17,-19,-24,-18,-36,-37,-29,-9,-32,-30,-31,]),'GT':([26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,54,80,81,96,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,147,150,151,],[-76,-77,-88,-83,-87,-53,76,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,97,-53,-52,145,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-5,-93,-94,]),'XOR':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,90,90,90,90,90,90,90,90,90,90,90,90,90,90,-90,-5,-93,-94,]),'RBRACE':([5,8,12,14,49,50,55,57,58,59,62,66,97,145,164,165,167,169,171,173,174,175,],[-16,-25,-26,-27,-21,-22,-20,-23,-17,-19,-24,-18,-36,-37,167,168,-29,171,-32,-30,175,-31,]),'FOR':([0,5,8,12,14,15,49,50,55,57,58,59,62,66,97,145,158,159,164,165,166,167,169,171,172,173,174,175,],[17,-16,-25,-26,-27,17,-21,-22,-20,-23,-17,-19,-24,-18,-36,-37,17,17,17,17,17,-29,17,-32,17,-30,17,-31,]),'EQUALS':([13,20,],[56,-95,]),'TIMES':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,87,87,87,87,87,87,87,87,87,87,87,87,87,87,-90,-5,-93,-94,]),'WRITE':([0,5,8,12,14,15,49,50,55,57,58,59,62,66,97,145,158,159,164,165,166,167,169,171,172,173,174,175,],[18,-16,-25,-26,-27,18,-21,-22,-20,-23,-17,-19,-24,-18,-36,-37,18,18,18,18,18,-29,18,-32,18,-30,18,-31,]),'GE':([26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,80,81,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,147,150,151,],[-76,-77,-88,-83,-87,-53,75,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,-53,-52,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-5,-93,-94,]),'LAND':([26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,80,81,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,147,150,151,],[-76,-77,-88,-83,-87,-53,77,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,-53,-52,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-5,-93,-94,]),'LPAREN':([2,17,18,20,21,22,25,39,40,51,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,144,148,161,],[39,60,39,63,64,39,69,39,63,95,39,39,39,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,155,39,155,]),'ELSE':([167,],[170,]),'EQ':([26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,80,81,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,147,150,151,],[-76,-77,-88,-83,-87,-53,78,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,-53,-52,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-5,-93,-94,]),'ID':([0,2,5,7,8,10,12,14,15,18,22,25,39,47,49,50,55,56,57,58,59,60,62,63,64,66,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,95,97,139,145,146,148,154,158,159,164,165,166,167,169,171,172,173,174,175,],[20,40,-16,51,-25,53,-26,-27,20,40,40,40,40,40,-21,-22,-20,40,-23,-17,-19,100,-24,40,40,-18,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,144,-36,40,-37,40,40,161,20,20,20,20,20,-29,20,-32,20,-30,20,-31,]),'IF':([0,5,8,12,14,15,49,50,55,57,58,59,62,66,97,145,158,159,164,165,166,167,169,170,171,172,173,174,175,],[21,-16,-25,-26,-27,21,-21,-22,-20,-23,-17,-19,-24,-18,-36,-37,21,21,21,21,21,-29,21,21,-32,21,-30,21,-31,]),'AND':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,83,83,83,83,83,83,83,83,83,83,83,83,83,83,-90,-5,-93,-94,]),'LOR':([26,27,28,29,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,80,81,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,147,150,151,],[-76,-77,-88,-83,-87,-53,74,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,-52,-53,-52,-74,-72,-62,-71,-61,-70,-60,-67,-57,-66,-56,-64,-54,-69,-59,-73,-63,-65,-55,-68,-58,-90,-5,-93,-94,]),'LBRACE':([149,153,163,170,],[158,159,166,172,]),'FALSE':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'READD':([0,5,8,12,14,15,49,50,55,57,58,59,62,66,97,145,158,159,164,165,166,167,169,171,172,173,174,175,],[22,-16,-25,-26,-27,22,-21,-22,-20,-23,-17,-19,-24,-18,-36,-37,22,22,22,22,22,-29,22,-32,22,-30,22,-31,]),'INT':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,82,83,84,85,86,87,88,89,90,91,92,139,146,148,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,117,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'FLOAT':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'RBRACKET':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,93,94,117,118,140,147,150,151,152,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,140,-91,150,151,-90,-5,-93,-94,-92,]),'NOP':([0,5,8,12,14,15,49,50,55,57,58,59,62,66,97,145,158,159,164,165,166,167,169,171,172,173,174,175,],[23,-16,-25,-26,-27,23,-21,-22,-20,-23,-17,-19,-24,-18,-36,-37,23,23,23,23,23,-29,23,-32,23,-30,23,-31,]),'OR':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,84,84,84,84,84,84,84,84,84,84,84,84,84,84,-90,-5,-93,-94,]),'MOD':([26,27,28,29,31,34,35,36,37,38,40,41,42,43,44,45,46,70,81,106,120,122,124,126,128,130,132,134,136,138,140,147,150,151,],[-76,-77,-88,-83,-87,-82,-79,-75,-86,-78,-95,-80,-89,-84,-85,-81,92,92,92,92,92,92,92,92,92,92,92,92,92,92,-90,-5,-93,-94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([0,9,],[1,52,]),'fun_pointer':([95,154,],[141,160,]),'readd':([0,15,158,159,164,165,166,169,172,174,],[3,3,3,3,3,3,3,3,3,3,]),'int':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'tree_get':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'float':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'funcall':([0,2,15,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,158,159,164,165,166,169,172,174,],[4,41,4,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,4,4,4,4,4,4,4,4,]),'ex':([0,15,158,159,164,165,166,169,172,174,],[5,58,5,5,58,58,5,58,5,58,]),'file':([0,],[6,]),'array':([47,],[93,]),'if':([0,15,158,159,164,165,166,169,170,172,174,],[8,8,8,8,8,8,8,8,173,8,8,]),'functions':([0,],[9,]),'bool_ex':([2,18,22,39,56,63,64,148,],[30,30,30,79,30,30,30,30,]),'op_ex':([2,18,22,25,39,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,148,],[32,32,32,67,80,32,32,32,105,67,67,67,67,67,67,67,67,119,121,123,125,127,129,131,133,135,137,32,]),'bool_value':([2,18,22,25,39,56,63,64,71,72,73,74,75,76,77,78,148,],[33,33,33,68,33,33,33,33,107,108,109,110,111,112,113,114,33,]),'array_get':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'write':([0,15,158,159,164,165,166,169,172,174,],[11,11,11,11,11,11,11,11,11,11,]),'fun_params':([95,],[142,]),'bool':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'foreach':([0,15,158,159,164,165,166,169,172,174,],[12,12,12,12,12,12,12,12,12,12,]),'var':([0,2,15,18,22,25,39,47,56,60,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,158,159,164,165,166,169,172,174,],[13,36,13,36,36,36,36,36,36,99,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,13,13,13,13,13,13,13,13,]),'readd_esc':([0,15,158,159,164,165,166,169,172,174,],[14,14,14,14,14,14,14,14,14,14,]),'empty':([63,95,],[101,143,]),'body':([0,158,159,166,172,],[15,164,165,169,174,]),'return':([0,15,158,159,164,165,166,169,172,174,],[16,16,16,16,16,16,16,16,16,16,]),'string':([2,10,18,22,25,39,47,53,56,63,64,69,71,72,73,74,75,76,77,78,82,83,84,85,86,87,88,89,90,91,92,139,146,148,],[38,54,38,38,38,38,38,96,38,38,38,38,38,38,38,38,38,38,38,38,118,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'nop':([0,15,158,159,164,165,166,169,172,174,],[19,19,19,19,19,19,19,19,19,19,]),'funcall_params':([63,],[102,]),'list':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'value':([2,18,22,25,39,47,56,63,64,69,71,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,139,146,148,],[46,46,46,70,81,94,46,46,46,106,70,70,70,70,70,70,70,70,120,122,124,126,128,130,132,134,136,138,152,156,46,]),'expression':([2,18,22,56,63,64,148,],[48,61,65,98,103,104,157,]),'assign':([0,15,158,159,164,165,166,169,172,174,],[24,24,24,24,24,24,24,24,24,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> file","S'",1,None,None,None),
  ('file -> functions','file',1,'p_file','parser.py',67),
  ('file -> body','file',1,'p_file','parser.py',68),
  ('functions -> function','functions',1,'p_functions','parser.py',80),
  ('functions -> functions function','functions',2,'p_functions','parser.py',81),
  ('funcall -> ID LPAREN funcall_params RPAREN','funcall',4,'p_funcall','parser.py',89),
  ('funcall_params -> empty','funcall_params',1,'p_funcall_params','parser.py',94),
  ('funcall_params -> expression','funcall_params',1,'p_funcall_params','parser.py',95),
  ('funcall_params -> funcall_params COMMA expression','funcall_params',3,'p_funcall_params','parser.py',96),
  ('function -> DEF ID LPAREN fun_params RPAREN LBRACE body RBRACE','function',8,'p_function','parser.py',107),
  ('fun_params -> empty','fun_params',1,'p_fun_params','parser.py',111),
  ('fun_params -> ID','fun_params',1,'p_fun_params','parser.py',112),
  ('fun_params -> fun_pointer','fun_params',1,'p_fun_params','parser.py',113),
  ('fun_params -> fun_params COMMA fun_pointer','fun_params',3,'p_fun_params','parser.py',114),
  ('fun_params -> fun_params COMMA ID','fun_params',3,'p_fun_params','parser.py',115),
  ('fun_pointer -> ID LPAREN RPAREN','fun_pointer',3,'p_fun_pointer','parser.py',126),
  ('body -> ex','body',1,'p_body','parser.py',130),
  ('body -> body ex','body',2,'p_body','parser.py',131),
  ('ex -> assign SEMI','ex',2,'p_ex','parser.py',142),
  ('ex -> return SEMI','ex',2,'p_ex','parser.py',143),
  ('ex -> write SEMI','ex',2,'p_ex','parser.py',144),
  ('ex -> readd SEMI','ex',2,'p_ex','parser.py',145),
  ('ex -> funcall SEMI','ex',2,'p_ex','parser.py',146),
  ('ex -> readd_esc SEMI','ex',2,'p_ex','parser.py',147),
  ('ex -> nop SEMI','ex',2,'p_ex','parser.py',148),
  ('ex -> if','ex',1,'p_ex','parser.py',149),
  ('ex -> foreach','ex',1,'p_ex','parser.py',150),
  ('ex -> readd_esc','ex',1,'p_ex','parser.py',151),
  ('nop -> NOP','nop',1,'p_nop','parser.py',156),
  ('if -> IF LPAREN expression RPAREN LBRACE body RBRACE','if',7,'p_if','parser.py',160),
  ('if -> IF LPAREN expression RPAREN LBRACE body RBRACE ELSE if','if',9,'p_if','parser.py',161),
  ('if -> IF LPAREN expression RPAREN LBRACE body RBRACE ELSE LBRACE body RBRACE','if',11,'p_if','parser.py',162),
  ('foreach -> FOR LPAREN var COLON value RPAREN LBRACE body RBRACE','foreach',9,'p_foreach','parser.py',172),
  ('return -> RETURN expression','return',2,'p_return','parser.py',176),
  ('write -> WRITE expression','write',2,'p_write','parser.py',180),
  ('readd -> READD expression','readd',2,'p_readd','parser.py',184),
  ('readd_esc -> LT string GT','readd_esc',3,'p_readd_esc','parser.py',188),
  ('readd_esc -> LT ID string GT','readd_esc',4,'p_readd_esc_parse','parser.py',192),
  ('assign -> var EQUALS expression','assign',3,'p_assign','parser.py',196),
  ('expression -> value','expression',1,'p_expression','parser.py',204),
  ('expression -> bool_ex','expression',1,'p_expression','parser.py',205),
  ('expression -> op_ex','expression',1,'p_expression','parser.py',206),
  ('bool_ex -> bool_value EQ bool_value','bool_ex',3,'p_bool_ex','parser.py',210),
  ('bool_ex -> bool_value NE bool_value','bool_ex',3,'p_bool_ex','parser.py',211),
  ('bool_ex -> bool_value LE bool_value','bool_ex',3,'p_bool_ex','parser.py',212),
  ('bool_ex -> bool_value GE bool_value','bool_ex',3,'p_bool_ex','parser.py',213),
  ('bool_ex -> bool_value LT bool_value','bool_ex',3,'p_bool_ex','parser.py',214),
  ('bool_ex -> bool_value GT bool_value','bool_ex',3,'p_bool_ex','parser.py',215),
  ('bool_ex -> bool_value LOR bool_value','bool_ex',3,'p_bool_ex','parser.py',216),
  ('bool_ex -> bool_value LAND bool_value','bool_ex',3,'p_bool_ex','parser.py',217),
  ('bool_ex -> LNOT bool_value','bool_ex',2,'p_bool_ex_2','parser.py',221),
  ('bool_ex -> LPAREN bool_ex RPAREN','bool_ex',3,'p_bool_ex_2','parser.py',222),
  ('bool_value -> value','bool_value',1,'p_bool_value','parser.py',229),
  ('bool_value -> op_ex','bool_value',1,'p_bool_value','parser.py',230),
  ('op_ex -> value PLUS value','op_ex',3,'p_op_ex','parser.py',234),
  ('op_ex -> value MINUS value','op_ex',3,'p_op_ex','parser.py',235),
  ('op_ex -> value TIMES value','op_ex',3,'p_op_ex','parser.py',236),
  ('op_ex -> value DIVIDE value','op_ex',3,'p_op_ex','parser.py',237),
  ('op_ex -> value MOD value','op_ex',3,'p_op_ex','parser.py',238),
  ('op_ex -> value LSHIFT value','op_ex',3,'p_op_ex','parser.py',239),
  ('op_ex -> value RSHIFT value','op_ex',3,'p_op_ex','parser.py',240),
  ('op_ex -> value OR value','op_ex',3,'p_op_ex','parser.py',241),
  ('op_ex -> value AND value','op_ex',3,'p_op_ex','parser.py',242),
  ('op_ex -> value XOR value','op_ex',3,'p_op_ex','parser.py',243),
  ('op_ex -> value PLUS op_ex','op_ex',3,'p_op_ex','parser.py',245),
  ('op_ex -> value MINUS op_ex','op_ex',3,'p_op_ex','parser.py',246),
  ('op_ex -> value TIMES op_ex','op_ex',3,'p_op_ex','parser.py',247),
  ('op_ex -> value DIVIDE op_ex','op_ex',3,'p_op_ex','parser.py',248),
  ('op_ex -> value MOD op_ex','op_ex',3,'p_op_ex','parser.py',249),
  ('op_ex -> value LSHIFT op_ex','op_ex',3,'p_op_ex','parser.py',250),
  ('op_ex -> value RSHIFT op_ex','op_ex',3,'p_op_ex','parser.py',251),
  ('op_ex -> value OR op_ex','op_ex',3,'p_op_ex','parser.py',252),
  ('op_ex -> value AND op_ex','op_ex',3,'p_op_ex','parser.py',253),
  ('op_ex -> value XOR op_ex','op_ex',3,'p_op_ex','parser.py',254),
  ('op_ex -> LPAREN op_ex RPAREN','op_ex',3,'p_op_ex_2','parser.py',258),
  ('value -> var','value',1,'p_value','parser.py',265),
  ('value -> int','value',1,'p_value','parser.py',266),
  ('value -> float','value',1,'p_value','parser.py',267),
  ('value -> string','value',1,'p_value','parser.py',268),
  ('value -> bool','value',1,'p_value','parser.py',269),
  ('value -> funcall','value',1,'p_value','parser.py',270),
  ('value -> list','value',1,'p_value','parser.py',271),
  ('value -> array_get','value',1,'p_value','parser.py',272),
  ('value -> tree_get','value',1,'p_value','parser.py',273),
  ('int -> INT','int',1,'p_int','parser.py',278),
  ('float -> FLOAT','float',1,'p_float','parser.py',282),
  ('string -> STRING','string',1,'p_string','parser.py',286),
  ('string -> MULTI_STRING','string',1,'p_multi_string','parser.py',290),
  ('bool -> TRUE','bool',1,'p_bool_true','parser.py',294),
  ('bool -> FALSE','bool',1,'p_bool_false','parser.py',298),
  ('list -> LBRACKET array RBRACKET','list',3,'p_list','parser.py',302),
  ('array -> value','array',1,'p_array','parser.py',307),
  ('array -> array COMMA value','array',3,'p_array','parser.py',308),
  ('array_get -> ID LBRACKET INT RBRACKET','array_get',4,'p_array_get','parser.py',316),
  ('tree_get -> ID LBRACKET string RBRACKET','tree_get',4,'p_tree_get','parser.py',320),
  ('var -> ID','var',1,'p_var','parser.py',324),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',328),
]
