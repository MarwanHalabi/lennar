```mermaid
classDiagram
    class Truck {
        +int id
        +float length
        +float width
        +float height
        +float volume()
    }

    class Package {
        +int id
        +float length
        +float width
        +float height
        +int? truck_id
        +float volume()
    }

    Truck "1" <-- "0..*" Package : contains
