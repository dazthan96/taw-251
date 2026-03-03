const nombre: string = "Hector";
let edad: number = 25;
let texto1: string =`Mi nombre es ${nombre} y el año que viene cumplire ${edad +1}`;
console.log(texto1);

function saludo(x:string):string{
    return `Hola ${x}`;
}
console.log(`Saludo: ${saludo(nombre)}`);