import { Injectable } from '@nestjs/common';
import { CreateProductDto } from './dto/create-product.dto';
import { UpdateProductDto } from './dto/update-product.dto';

export interface Producto{
  id:number;
  nombre:string;
  precio:number
}

@Injectable()
export class ProductService {
  private productos: Producto[]=[
    { id:1, nombre:"producto 1", precio:10 },
    { id:2, nombre:"producto 2", precio:20 },
    { id:3, nombre:"producto 3", precio:30 }
  ];
  create(createProductDto: CreateProductDto) {
    return 'This action adds a new product';
  }

  findAll():Producto[] {
    return this.productos;
  }

  findOne(id: number):Producto | undefined{
    const p1 = this.productos.find(producto => producto.id === id);
    return p1;
  }

  update(id: number, updateProductDto: UpdateProductDto) {
    return `This action updates a #${id} product`;
  }

  remove(id: number) {
    return `This action removes a #${id} product`;
  }
}
