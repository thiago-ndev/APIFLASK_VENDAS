from models.perfil_model import PerfilModel

p1 = PerfilModel(sigla= "FRONT", perfil="FRONTEND")
p1.save()

p2 = PerfilModel(sigla= "APP", perfil="Mobile")
p2.save()

p3 = PerfilModel(sigla="ADMIN", perfil="Administrador")
p3.save()

p4 = PerfilModel(sigla="USER", perfil="Usuario")
p4.save()

p5 = PerfilModel(sigla="CLI", perfil="Cliente")
p5.save()

PerfilModel.query.all()

