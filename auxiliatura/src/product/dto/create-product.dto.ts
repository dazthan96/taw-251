import { IsNumber, IsString } from "class-validator";

export class CreateProductDto {
    @IsString()
    nombre:string;
    @IsNumber()
    costo:number
}
