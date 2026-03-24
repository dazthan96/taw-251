//forma tradicional
/*
class Rectangulo{
    //atributos y metodos
    public base:number;
    public altura:number;
    public constructor (base:number,altura:number){
        this.base=base,
        this.altura=altura
    }
    //metodos
    public area():number{
        return this.base * this.altura;
    }
}
const rectagulo1 = new Rectangulo(10,2);

console.log('Area del rectangulo = ',rectagulo1.area());
*/
//forma corta

class Rectangulo{
    public constructor (public base:number,public altura:number){ }
    //metodos
    public area():number{
        return this.base * this.altura;
    }
}
const rectagulo1 = new Rectangulo(10,2);
console.log('Area del rectangulo = ',rectagulo1.area());
//Sobre la clase Rectangulo agregar un setter y getter de los atributos
//Agregar clase padre Figura que tendra un atributo color de tipo string
export{}