

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result

    def show_query_result(self):
        for d in self.query_result:
            print(str(d))
    
    # 1.1
    def list_associations(self):
        return list(set([d.relation.name for d in self.declarations if isinstance(d.relation, Association)]))

    # 1.2
    def list_objects(self):
        return list(set([d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)]))

    # 1.3
    def list_users(self):
        return list(set([d.user for d in self.declarations]))
    
    
    # 1.4
    def list_types(self):
        return list(set(
            [d.relation.entity1 for d in self.declarations if isinstance(d.relation, Subtype)] +
            [d.relation.entity2 for d in self.declarations if isinstance(d.relation, Member) or isinstance(d.relation, Subtype)]
        ))

    # 1.5
    def list_local_associations(self, entity):
        return list(set(d.relation.name for d in self.declarations if isinstance(d.relation, Association) and entity in [d.relation.entity1, d.relation.entity2]))

    # 1.6
    def list_relations_by_user(self, user):
        return list(set(d.relation.name for d in self.declarations if d.user == user))

    # 1.7
    def associations_by_user(self, user):
        return len(set([d.relation.name for d in self.declarations if isinstance(d.relation, Association) and d.user==user]))

    # 1.8
    def list_local_associations_by_user(self, entity):
        return list(set([(d.relation.name, d.user) for d in self.declarations if isinstance(d.relation, Association) and entity in [d.relation.entity1, d.relation.entity2]]))

    # 1.9
    def predecessor(self, A, B):
        predec_b = [d.relation.entity2 for d  in self.declarations if isinstance(d.relation, (Member, Subtype)) and d.relation.entity1 == B]
        return A in predec_b or any([self.predecessor(A, p) for p in predec_b])

    # 1.10
    def predecessor_path(self, A, B):
        if not self.predecessor(A, B):
            return None
        predec_b = [d.relation.entity2 for d in self.declarations if isinstance(d.relation, (Member, Subtype)) and d.relation.entity1 == B]

        if A in predec_b:
            return [A, B]
        
        for predec in predec_b:
            path = self.predecessor_path(A, predec)
            if path != None:
                return path + [B]
        return None

    # 1.11a
    def query(self, entity, assoc = None):
        parents = [d.relation.entity2 for d in self.declarations if isinstance(d.relation, (Member, Subtype)) and d.relation.entity1 == entity]
        
        ldecl = [d for d in self.query_local(e1 = entity, rel = assoc) if isinstance(d.relation, Association)]
        for p in parents:
            ldecl += self.query(p, assoc)
        return ldecl

    # 1.11b
    def query2(self, entity, rel = None):
        ldecl = [d for d in self.query_local(e1 = entity, rel = rel) if not isinstance(d.relation, Association)]
        return ldecl + self.query(entity, rel)


        

# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

