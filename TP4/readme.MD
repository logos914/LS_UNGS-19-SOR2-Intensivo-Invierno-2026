# TP4 — PROTOCOLOS Y SEGURIDAD EN REDES SOR2 2S 2026 Intensivo
## Universidad Nacional de General Sarmiento
## Licenciatura en Sistemas
## Sistemas Operativos y Redes 2 (A0533)
### Año y semestre: 
Intensivo Invierno 2026
### Profesor: 
- Benjamín Chuquimango
### Integrantes: 
- David Ezequiel Cañete 
- Ignacio Mariano Tula


# Índice
@todo



# SECCIÓN 1 — Introducción (½ página)

## 1.1 Contexto y objetivo del trabajo
@todo
## 1.2 Distribución de tareas entre integrantes
@todo

Tabla de distribución:
|*Integrante* | *Tarea a Cargo* |
| ------------- | ------------- |
| David Cañete | @todo | 
| Ignacio Tula | @todo | 


# SECCIÓN 2 — Entorno de Trabajo

## 2.1 Sistema operativo (salida de uname -a y cat /etc/os-release)

![´´´uname -a && cat /etc/os-release´´](capturas/2/2-1.jpg)


## 2.2 Recursos de la VM (RAM, disco, CPU asignados)
![Recursos de VirtualBox asignados](capturas/2/2-2-vm-resources.png)
## 2.3 Herramientas utilizadas (nombre y versión de cada herramienta relevante)

### 2.3.1 Preparación de la VM para escrbir en repo
![](capturas/2/2-2-sshkeygen.jpg)

## 2.4 Estado inicial del sistema (capturas del estado "antes" según lo indicado en el enunciado de
cada TP)

# SECCIÓN 3 - Seguridad en HTTPS, Certificados y Autoridad Certificante

## 3.1 Primera Parte: Instalación de Servidor LAMP

### 3.1.1 Instalación de apache

Se instaló el servidor web Apache con
```bash
sudo apt-get install apache2 -y > archivo.txt
```

[Salida de Instalación de Apache](capturas/3/3-1-1.txt)


### 3.1.2 Configuración de Apache

Se revisó el contenido de los archivos de configuración

- `/etc/apache/apache2.conf` 
- `/etc/apache/ports.conf` 

![apache2.conf](capturas/3/3-1-2-1.jpg)
Contenido de: [apache2.conf](capturas/3/apache2.conf)

![apache2.conf](capturas/3/3-1-2-2.jpg)
Contenido de: [ports.conf](capturas/3/ports.conf)

### 3.1.3 Configuración de sitios virtuales

Se ejecutaron los siguientes comandos para crear las carpetas de los virtual hosts, y asignarle permisos adecuados a nuestro usuario

![Virtual Hosts](capturas/3/3-1-3-1.jpg)

Se crearon archivos index.html para cada empresa. Cada uno en su respectivo `/var/www/empresax/public_html`

- Empresa 1: [index.html](capturas/3/empresa1/index.html)
- Empresa 2: [index.html](capturas/3/empresa2/index.html)