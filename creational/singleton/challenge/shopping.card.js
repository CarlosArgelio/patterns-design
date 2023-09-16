class Product {
    constructor(id, name, cost) {
        this._id = id;
        this._name = name;
        this._cost = cost;
    };

    getName() {
        return this._name
    }

    getCost() {
        return this._cost
    }

    getId() {
        return this._id
    }
};

class ShoppingCar {
    static instance = undefined;
    constructor() {
        this._products = [];
    }

    static getInstance() {
        if (!ShoppingCar.instance) {
            ShoppingCar.instance = new ShoppingCar();
        }
        return ShoppingCar.instance;
    }

    addProduct(product) {
        this._products.push(product);
    }

    getProductById(id) {
        return this._products.find(product => product._id === id)
    }

    deleteById(id) {
        const product = this.getProductById(id)
        const index = this._products.indexOf(product)
        this._products.splice(index, 1)
    }

    getAllProduct() {
        return this._products
    }
};

(function clienteApp() {
    const cart = ShoppingCar.getInstance();
    const vasos = new Product(1, "vasos plasticos" , 3)
    const zapatos = new Product(2, "gomas deportivas" , 30)
    const franela = new Product(3, "franela azul" , 25)
    const gorra = new Product(4, "gorra americana" , 10)
    const shorts = new Product(5, "shorts rojos" , 15)    

    cart.addProduct(vasos)
    cart.addProduct(zapatos)
    cart.addProduct(franela)
    cart.addProduct(gorra)
    /* Validamos que hay productos en el carrito */
    console.log(cart.getAllProduct);
    
    /* Instanciamos un segundo carrito y validamos que ya tiene productos*/
    const cart2 = ShoppingCar.getInstance();
    console.log(cart2.getAllProduct);
    /* Le agregamos un producto */
    cart2.addProduct(shorts);
    console.log(cart2.getAllProduct())
    /* Eliminamos un producto */
    console.log('Eliminamos exitosament el producto', cart.deleteProduct(2))

    /* Validamos que se elimino en ambos carritos */    
    console.log(cart.getAllProduct(),)
    console.log(cart2.getAllProduct())
})()