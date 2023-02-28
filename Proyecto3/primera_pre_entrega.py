B_D={}

def registrar_user():
  #Solicitamos el usuario y la contraseña.
  user_registro= input("Ingrese un nuevo usuario a validar: ")
  pass_registro = input("Coloque aqui una contraseña a registrar: ")
  B_D[user_registro]=pass_registro

  while True:
    pregunta = input('¿Desea seguir cargando usarios?  si-no : ')
    if pregunta == 'si':
      user_registro= input("Ingrese un nuevo usuario a validar: ")
      pass_registro = input("Coloque aqui una contraseña a registrar: ")
      B_D[user_registro]=pass_registro

    else:
      break
  return (f"Usuario/s registrados correctamente")

def registro():
  #Solicitamos que ingresen un nombre de usuario.
    login_user= input("Ingrese su usuario aqui : ")

    #Si el usuario está en la B_D va a ingresar.
    if login_user in personas:

      #Una vez que ingresa es porque el usuario existe, ahora sólo toca pedir la contraseña.
      login_pwd= input("Ingrese su contraseña aqui : ")

      #Verificamos si la contraseña ingresada coincide con la contraseña registrada en nuestra B_D
      if B_D[login_user] == login_pwd:
        #Si la contraseña es correcta, retornamos un mensaje de BIENVENIDA.
        return( f"Ingreso al sistema de forma correcto, bienvenido {login_user} ")
      else:
        return ("Contraseña Incorrecta")
    else:
      #Sino retorna el mensaje -->  Usuario no encontrado
      return 'Usuario no encontrado'
print(B_D)
print(registrar_user())
print(B_D)
print(registro())