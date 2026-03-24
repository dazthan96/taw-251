/*type Color = 'rojo'|'verde'|'azul';
interface Persona{
    id:number,
    nombre:string,
    color:Color
}
const personas:Persona[] = [
    {
    id:1,
    nombre:"Rosmery",
    color:'azul'},
    {
        id:2,
        nombre:"Anabel",
        color:"verde"
    }
]; 
console.log(personas)
*/
//orignal solo con los valores

enum Colores {
    rojo = 'rojo', //0 original -si le damos valores al seleccionarlo seran los valores definidos, es como un diccionario en python
    verde='verde', //1 original -
    azul='azul'//2 orignal -
};
interface Persona{
    id:number,
    nombre:string,
    color:Colores
}
const personas:Persona[] = [
    {
    id:1,
    nombre:"Rosmery",
    color:Colores.azul},
    {
        id:2,
        nombre:"Anabel",
        color:Colores.rojo
    }
]; 
//console.log(Colores.rojo)//imprimira el indice del color dado
console.log(personas)
export {}
