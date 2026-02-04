# GEMINI API

Este proyecto contiene un script para conectarse a la API de Gemini utilizando Python.

---

## Requisitos

1. Python 3.11 o superior.
2. Entorno virtual configurado.
3. Clave de API de Gemini.

---

## Instalación

### Paso 1: Clonar el repositorio
Clona el repositorio desde GitHub: git clone https://github.com/Vivi271/GEMINI-API.git


### Paso 2: Navegar al directorio del proyecto: cd GEMINI-API

### Paso 3: Crear y activar un entorno virtual

1. **Crear el entorno virtual**:
   Un entorno virtual es necesario para aislar las dependencias del proyecto. Usa el siguiente comando para crearlo:

   python3 -m venv venv

   Esto creará una carpeta llamada venv en el directorio del proyecto.

2. **Activar el entorno virtual**:
   - En macOS/Linux: source venv/bin/activate
     
   - En Windows: venv\Scripts\activate

   Una vez activado, deberías ver `(venv)` al inicio de tu línea de comandos.

### Paso 4: Instalar las dependencias

    Instala las bibliotecas necesarias desde el archivo requirements.txt: pip install -r requirements.txt

    Si no tienes el archivo requirements.txt, puedes generarlo con: pip freeze > requirements.txt

### Paso 5: Configurar la clave de API

    Crea un archivo .env en la raíz del proyecto y agrega tu clave de API: GEMINI_API_KEY=tu_clave_de_api

## Solución de problemas

### Error: `ModuleNotFoundError`
   
    Si aparece un error indicando que falta una biblioteca, asegúrate de que el entorno virtual esté activado y vuelve a instalar las dependencias:
    
      source venv/bin/activate
      pip install -r requirements.txt

### Error: `Python no encontrado`
    Si tu sistema no encuentra Python, verifica que esté instalado correctamente y que el comando `python3` esté disponible. En macOS/Linux, puedes instalar Python con:

      brew install python


### Error: `Problemas con pip`
    Si aparece un error relacionado con `pip`, actualízalo:

      pip install --upgrade pip

## Ejecución
    
    Ejecuta el script con el siguiente comando:

      python app_gemini.py


---

## Evidencia
<img width="2900" height="2118" alt="image" src="https://github.com/user-attachments/assets/2b65cbd0-71d2-4b77-b50e-b2b77aefdf1d" />

