//de un arreglo de objeto producto (nombre, precio) obtener la suma de los precios de todos los productos. utilice una funcion flecha
interface Producto{
    nombre:string;
    precio:number
}
const productos:Array<Producto>=[
    {
        nombre:"dulce de leche",
        precio:10
    },
    {
        nombre:"leche",
        precio:20
    },
    {
        nombre:"caramelos",
        precio:30
    },
    {
        nombre:"chocolate",
        precio:40
    }
]
const sumaPrecio = productos.reduce((total, productos)=>productos.precio+total,0)
console.log(sumaPrecio)
    
    
