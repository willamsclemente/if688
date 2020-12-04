# Generated from antlr4-python3-runtime-4.7.2/src/autogen/Grammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

'''
COMO RESGATAR INFORMAÇÕES DA ÁRVORE

Observe o seu Grammar.g4. Cada regra sintática gea uma função com o nome corespondente no Visitor e na ordem em que está na gramática. Para deixar na ordem em que você colocou, substitua as funções dentro de "class GrammarCheckerVisitor(ParseTreeVisitor)" pelas que apareem em autogem/GrammarVisitor.g4 depois do make ser rodado. Mas antes algumas mudanças precisam ser feitas em Grammar.g4. Primeiro copie-a do projeto1 para o projeto2. Depois adicione o tipo "VOID: 'void'" no lexer e na regra de "type" no parser (só "| VOID" aqui). Agora, por causa de conflitos com Python, substitua as regras file por fiile e type por type ("make adjust" substitui automaticamente). Use prints temporários para ver se está no caminho certo.  "make tree" agora desenha a árvore sintática, se quiser vê-la para qualquer input, enquanto "make" roda este visitor sobre o a árvore gerada a partir de Grammar.g4 alimentada pelo input.


expr = ctx.expression().accept(self)  # entra no nó expression e seus filhos e retorna alguma coisa

for i in range(len(ctx.identifier())): # para cada identficador que este nó possui...
    ident = ctx.identifier()[i].accept(self) # ...pegue o i-ésimo

if ctx.FLOAT() != None: # se houver um FLOAT (em vez de INT ou VOID) neste nó (parser)
    return Type.FLOAT # retorne float
'''

# retorne Type.INT, etc para fazer checagem de tipos
class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    STRING = "string"

class GrammarCheckerVisitor(ParseTreeVisitor):
    ids_defined = {} # armazenar informações necessárias para cada identifier definido
    
    ids_undefined = {} #armezenar informações necessárias para cada identifier não inicializado

    
    # Visit a parse tree produced by GrammarParser#fiile.
    def visitFiile(self, ctx:GrammarParser.FiileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_definition.
    def visitFunction_definition(self, ctx:GrammarParser.Function_definitionContext):
        if ctx.identifier() != None:
            text = ctx.identifier().getText()
            function_type = ctx.tyype().getText() 
            token = ctx.identifier().IDENTIFIER().getPayload()

            if (text in GrammarCheckerVisitor.ids_defined) == False:
                GrammarCheckerVisitor.ids_defined[text] = [function_type, len(ctx.arguments().identifier())]
            else:
                raise NameError("function definition '" + text + "'() linha: "+ str(token.line) + " ,já foi definido anteriormente.")

            for i in range(len(ctx.arguments().identifier())):
                text1 = ctx.arguments().identifier(i).getText()
                tyype = ctx.arguments().tyype(i).getText()
                token1 = ctx.arguments().identifier(i).IDENTIFIER().getPayload()

                if (text1 in GrammarCheckerVisitor.ids_defined) == False:
                    GrammarCheckerVisitor.ids_defined[text1] = tyype
                    GrammarCheckerVisitor.ids_defined[text].append(text1)
                else:
                    raise NameError("identifier'" + text + "' linha: "+ str(token1.line) + " ,já foi definido anteriormente.")
            
            key = 0
            for i in range(len(ctx.body().statement())):

                if 'return' == ctx.body().statement(i).children[0].getText():
                    key = 1
                    if function_type == Type.VOID:
                        raise NameError("function definition '" + text + "'() linha: "+ str(token.line) + " ,não possui retorno.")

                    else:
                        expr_type = self.visit(ctx.body().statement(i).expression())

                        if expr_type != function_type:
                            if (function_type == Type.INT and expr_type == Type.FLOAT) or (function_type == Type.FLOAT and expr_type == Type.INT) :
                                print("WARNING: function definition '" + text + "'() linha: "+ str(token.line) + " ,pode perder informações, por retorna um tipo diferente da definição da função")
                            else:
                                 raise NameError("function definition '" + text + "'() linha: "+ str(token.line) + " ,retorna um tipo diferente da definição da função.")
                    
                else: 
                    self.visit(ctx.body().statement(i))
            
            if key == 0  and function_type != Type.VOID:
                raise NameError("function definition '" + text + "'() linha: "+ str(token.line) + " ,não está retornando nada.")


                        
    # Visit a parse tree produced by GrammarParser#body.
    def visitBody(self, ctx:GrammarParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        
        if ctx.variable_definition() != None:
            self.visit(ctx.variable_definition())

        elif ctx.variable_assignment() != None:
            self.visit(ctx.variable_assignment())

        elif ctx.expression() != None:
            tyype = self.visit(ctx.expression())
        
        elif ctx.for_loop() != None:
            self.visit(ctx.for_loop())
        
        elif ctx.if_statement() != None:
            self.visit(ctx.if_statement())
        
        elif ctx.body() != None:
            self.visit(ctx.body())


    # Visit a parse tree produced by GrammarParser#if_statement.
    def visitIf_statement(self, ctx:GrammarParser.If_statementContext):
    
        if ctx.expression() != None:
            tyype = self.visit(ctx.expression())
        
        if ctx.body() != None:
            self.visit(ctx.body())
        else:
            self.visit(ctx.statement())

        if ctx.else_statement() != None:
            self.visit(ctx.else_statement())



    # Visit a parse tree produced by GrammarParser#else_statement.
    def visitElse_statement(self, ctx:GrammarParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_loop.
    def visitFor_loop(self, ctx:GrammarParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_initializer.
    def visitFor_initializer(self, ctx:GrammarParser.For_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_condition.
    def visitFor_condition(self, ctx:GrammarParser.For_conditionContext):
        
        if ctx.expression() != None:
            tyype = self.visit(ctx.expression())
            
    # Visit a parse tree produced by GrammarParser#for_step.
    def visitFor_step(self, ctx:GrammarParser.For_stepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_definition.
    def visitVariable_definition(self, ctx:GrammarParser.Variable_definitionContext):
        
        for i in range(len(ctx.identifier())):
            
            if ctx.expression(i) != None:
                expr_type = self.visit(ctx.expression(i))
                tyype = ctx.tyype().getText() 
                text = ctx.identifier(i).getText()
                token = ctx.identifier(i).IDENTIFIER().getPayload()

                if  tyype == expr_type:
            
                    if (text in GrammarCheckerVisitor.ids_defined) == False:
                        GrammarCheckerVisitor.ids_defined[text] = tyype
                    else:
                        raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,já foi definido anteriormente.")

                elif (tyype == Type.INT and expr_type == Type.FLOAT) or (tyype == Type.FLOAT and expr_type == Type.INT):
                    print("WARNING: identifier '" + text + "' linha: "+ str(token.line) + " ,pode perder informações, por está recebendo um tipo diferente do tipo do identificador.")

                    if (text in GrammarCheckerVisitor.ids_defined) == False:
                        GrammarCheckerVisitor.ids_defined[text] = tyype
                    else:
                        raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,já foi definido anteriormente.")
                else:
                    raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,está recebendo um que tipo que não é aceito")
                   
            else: 
                text = ctx.identifier(i).getText()
                tyype = ctx.tyype().getText()
                token = ctx.identifier(i).IDENTIFIER().getPayload()

                if (text in GrammarCheckerVisitor.ids_defined) == False:
                    GrammarCheckerVisitor.ids_defined[text] = Type.VOID
                    GrammarCheckerVisitor.ids_undefined[text] = tyype
                else:
                    raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,já foi definido anteriormente.")

              
       
        for i in range(len(ctx.array())):
            
            if ctx.array_literal(i) != None:
                index_type = self.visit(ctx.array(i).expression())
                array_tyype = ctx.tyype().getText() 
                text = ctx.array(i).identifier().getText()
                token = ctx.array(i).identifier().IDENTIFIER().getPayload()
                
                if  index_type == Type.INT:

                    key = 0
                    for j in range(len(ctx.array_literal(i).expression())):
                        expr_type = self.visit(ctx.array_literal(i).expression(j))  

                        if expr_type != array_tyype:
                            key = 1  
                        if expr_type != Type.INT and  expr_type != Type.FLOAT:
                            key = 2
                        
                        
                    if key == 0:
                        if (text in GrammarCheckerVisitor.ids_defined) == False:
                            GrammarCheckerVisitor.ids_defined[text] = array_tyype
                        else:
                            raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,já definido anteriormente.")

                    elif key == 1:
                        print("WARNING: identifier '" + text + "'[] linha: "+ str(token.line) + " ,pode perder informações, por está recebendo um tipo diferente do tipo do array.")
                        if (text in GrammarCheckerVisitor.ids_defined) == False:
                            GrammarCheckerVisitor.ids_defined[text] = array_tyype
                        else:
                            raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,já definido anteriormente.")
            
                    else:
                        raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,está recebendo um tipo diferente do tipo do array")
                
                else:
                    raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,não possui índice do tipo 'int'.")        

            else:

                index_type = self.visit(ctx.array(i).expression())
                text = ctx.array(i).identifier().getText()
                array_tyype = ctx.tyype().getText() 
                token = ctx.array(i).identifier().IDENTIFIER().getPayload()

                if  index_type == Type.INT:
                     
                    if (text in GrammarCheckerVisitor.ids_defined) == False:
                        GrammarCheckerVisitor.ids_defined[text] = Type.VOID
                        GrammarCheckerVisitor.ids_undefined[text] = array_tyype
                    else:
                        raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,já definido anteriormente.")
            
                else:
                    raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,não possui índice do tipo 'int'.")


    # Visit a parse tree produced by GrammarParser#variable_assignment.
    def visitVariable_assignment(self, ctx:GrammarParser.Variable_assignmentContext):
    
        if ctx.expression() != None:
            
            key = 0
            if ctx.identifier() != None:
                key = 1
                text = ctx.identifier().getText()
                token = ctx.identifier().IDENTIFIER().getPayload()
                
                if (text in GrammarCheckerVisitor.ids_defined) == True:
                    tyype = GrammarCheckerVisitor.ids_defined[text]
                else:
                    raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,não foi definido ainda.")

            else:
                text = ctx.array().identifier().getText()
                token = ctx.array().identifier().IDENTIFIER().getPayload()

                if (text in GrammarCheckerVisitor.ids_defined) == True:
                    tyype = GrammarCheckerVisitor.ids_defined[text]
                else:
                    raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,não foi definido ainda.")


            expr_type = self.visit(ctx.expression())
                
            if (tyype == Type.INT and expr_type == Type.FLOAT) or (tyype == Type.FLOAT and expr_type == Type.INT):
                if key == 1:
                    print("WARNING: identifier '" + text + "' linha: "+ str(token.line) + " ,pode perder informações, por está recebendo um tipo diferente do tipo do identificador.")
                else:
                    print("WARNING: array '" + text + "'[] linha: "+ str(token.line) + " ,pode perder informações, por está recebendo um tipo diferente do tipo do array.") 
               
            elif tyype == Type.VOID and (expr_type == Type.INT or expr_type == Type.FLOAT):
                GrammarCheckerVisitor.ids_defined[text] =  GrammarCheckerVisitor.ids_undefined[text]
                tyype = GrammarCheckerVisitor.ids_defined[text]
                del GrammarCheckerVisitor.ids_undefined[text]

                if (tyype == Type.INT and expr_type == Type.FLOAT) or (tyype == Type.FLOAT and expr_type == Type.INT):
                    if key == 1:
                        print("WARNING: identifier '" + text + "' linha: "+ str(token.line) + " ,pode perder informações, por está recebendo um tipo diferente do tipo do identificador.")
                    else:
                        print("WARNING: array '" + text + "'[] linha: "+ str(token.line) + " ,pode perder informações, por está recebendo um tipo diferente do tipo do array.") 
                    
            else:
                if tyype != expr_type:
                    if key == 1:
                        raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,está recebendo um tipo diferente do aceito")
                    else:
                        raise NameError("array '" + text + "' linha: "+ str(token.line) + " ,está recebendo um tipo diferente do aceito")

        elif ctx.expression() == None:
            
            if ctx.identifier != None:
                text = ctx.identifier().getText()
                token = ctx.identifier().IDENTIFIER().getPayload()
                
                if (text in GrammarCheckerVisitor.ids_defined) == True:
                    tyype = GrammarCheckerVisitor.ids_defined[text]
                    if tyype != Type.INT and tyype != Type.float:
                        raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,não possui tipo 'int' ou 'float'.")
                else:
                    raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,não foi definido ainda.")
            
            else:
                text = ctx.array().identifier().getText()
                token = ctx.array().identifier().IDENTIFIER().getPayload()
                
                if (text in GrammarCheckerVisitor.ids_defined) == True:
                    tyype = GrammarCheckerVisitor.ids_defined[text]
                    if tyype != Type.INT and tyype != Type.float:
                        raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,não possui tipo 'int' ou 'float'.")
                else:
                    raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,não foi definido ainda.")


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):

        tyype = Type.VOID
        if len(ctx.expression()) == 0:

            if ctx.integer() != None:
                text = ctx.integer().getText()
                token = ctx.integer().INTEGER().getPayload()

                tyype = Type.INT

            elif ctx.floating() != None:
                text = ctx.floating().getText()
                token = ctx.floating().FLOATING().getPayload()

                tyype = Type.FLOAT

            elif ctx.string() != None:
                typpe = Type.STRING 

            elif ctx.identifier() != None:
                text = ctx.identifier().getText()
                token = ctx.identifier().IDENTIFIER().getPayload()

                if (text in GrammarCheckerVisitor.ids_defined) == True:
                    tyype = GrammarCheckerVisitor.ids_defined[text]
                else:
                    raise NameError("identifier '" + text + "' linha: "+ str(token.line) + " ,não foi definido ainda.")

            elif ctx.array() != None:
                text = ctx.array().identifier().getText()
                token = ctx.array().identifier().IDENTIFIER().getPayload()

                if (text in GrammarCheckerVisitor.ids_defined) == True:
                    tyype = GrammarCheckerVisitor.ids_defined[text]
                else:
                    raise NameError("array '" + text + "'[] linha: "+ str(token.line) + " ,não foi definido ainda.")

           
            elif ctx.function_call != None:
                text = ctx.function_call().identifier().getText()
                token = ctx.function_call().identifier().IDENTIFIER().getPayload()
                    
                if (text in GrammarCheckerVisitor.ids_defined) == True:
                    function = GrammarCheckerVisitor.ids_defined[text]
                    
                    if function[1] != len(ctx.function_call().expression()):
                        raise NameError("function call '" + text + "'() linha: "+ str(token.line) + " ,possui um número incorreto de argumentos.")


                    else:
                        for i in range(len(ctx.function_call().expression())):
                            arg_type = self.visit(ctx.function_call().expression(i))
                            arg_function = GrammarCheckerVisitor.ids_defined[function[i+2]]
                            if arg_type != arg_function:
                                if (arg_function == Type.INT and arg_type == Type.FLOAT) or (arg_function == Type.FLOAT and arg_type == Type.INT):
                                    print("WARNING: function call '" + text + "'() linha: "+ str(token.line) + " ,pode perder informações, por está passando um argumento de tipo diferente da definição da função")
                                else:
                                    raise NameError("function call '" + text + "'() linha: "+ str(token.line) + " ,está passando um argumento de tipo diferente do aceito.")


                        tyype = function[0]
               
                else:

                    for i in range(len(ctx.function_call().expression())):
                            arg_type = self.visit(ctx.function_call().expression(i))
                    
                    tyype = Type.VOID
                 
        
        elif len(ctx.expression()) == 1:

            if ctx.OP != None:
                text = ctx.OP.text
                token = ctx.OP

                tyype = self.visit(ctx.expression(0))
            
            else:
                tyype = self.visit(ctx.expression(0))

        elif len(ctx.expression()) == 2:
            text = ctx.OP.text
            token = ctx.OP
            
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))

            listaOpA = ['+', '-', '*', '/']
            listaOpL = ['<', '<=', '==', '>=', '>', '!=']
            
            if(left == Type.INT) and (right == Type.INT) and ((text in listaOpA) or (text in listaOpL)):
                tyype = Type.INT
            elif (left == Type.FLOAT) and (right == Type.FLOAT) and (text in listaOpA):
                tyype = Type.FLOAT
            elif (((left == Type.FLOAT) and (right == Type.INT)) or ((left == Type.INT) and (right == Type.FLOAT))) and (text in listaOpA): 
                tyype = Type.FLOAT
            elif (left == Type.FLOAT) and (right == Type.FLOAT) and (text in listaOpL):
                tyype = Type.FLOAT
            else:
                raise NameError("expression '" + text + "'() linha: "+ str(token.line)+ " ,possui operadores que não são do tipo 'int' ou 'float'.")
        
        return tyype



    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx:GrammarParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#array_literal.
    def visitArray_literal(self, ctx:GrammarParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_call.
    def visitFunction_call(self, ctx:GrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arguments.
    def visitArguments(self, ctx:GrammarParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#tyype.
    def visitTyype(self, ctx:GrammarParser.TyypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#integer.
    def visitInteger(self, ctx:GrammarParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#floating.
    def visitFloating(self, ctx:GrammarParser.FloatingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#string.
    def visitString(self, ctx:GrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#identifier.
    def visitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    #del GrammarParser

    #def aggregateResult(self, aggregate:Type, next_result:Type):
        #return next_result if next_result != None else aggregate
