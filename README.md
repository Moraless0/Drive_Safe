# 🚗 DriveSafe - Sistema de Gestión de Citas

DriveSafe es una aplicación en Python que permite gestionar clientes, instructores, vehículos y citas para una academia de conducción.

---

## 📌 Características

* 👤 Registro de clientes
* 👨‍🏫 Registro de instructores
* 🚗 Gestión de vehículos
* 📅 Programación de citas
* ✅ Registro de asistencia
* 📊 Reportes e historial
* 🔍 Búsqueda por cliente y fecha
* ⚠️ Validación de conflictos (instructor/vehículo ocupado)

---

## 🗂️ Estructura del Proyecto

```
DriveSafe/
│
├── data/
│   ├── clientes.json
│   ├── instructores.json
│   ├── vehiculos.json
│   └── citas.json
│
├── utilidades.py
├── main.py
└── README.md
```

---

## ⚙️ Requisitos

* Python 3.x
* Sistema operativo: Windows / Linux / Mac

---

## ▶️ Ejecución

1. Clona el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
```

2. Entra al proyecto:

```
cd DriveSafe
```

3. Ejecuta el programa:

```
python main.py
```

---

## 📊 Funcionalidades principales

### 📅 Gestión de Citas

* Crear citas validando:

  * Cliente existente
  * Instructor disponible
  * Vehículo disponible
* Evita conflictos de horario

### ✅ Asistencia

* Registrar si el cliente asistió
* Agregar observaciones

### 📊 Reportes

* Ver todas las citas
* Filtrar por cliente
* Filtrar por fecha
* Ver citas con/sin asistencia

---

## 🧠 Validaciones implementadas

* ❌ Cliente no existe
* ❌ Instructor no existe
* ❌ Tipo de vehículo no coincide
* ❌ Instructor ocupado
* ❌ Vehículo ocupado

---

## 💾 Almacenamiento

Toda la información se guarda en archivos `.json`, lo que permite:

* Fácil lectura
* Persistencia de datos
* Simplicidad en pruebas

---

## 🚀 Futuras mejoras

* ✏️ Editar citas
* ❌ Cancelar citas
* 📊 Estadísticas avanzadas
* 📄 Exportar reportes
* 🖥️ Interfaz gráfica (GUI)

---

## 👨‍💻 Autor

Henry Morales

---

## 📄 Licencia

Este proyecto es de uso educativo.
