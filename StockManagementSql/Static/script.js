function checkInput() {

    let input1 = document.getElementById("product_name_add").value;
    let input2 = document.getElementById("product_price_add").value;
    let input3 = document.getElementById("product_quantity_add").value;
    let check = input1 === "" || input2 === "" || input3 === "";
    if (check == true ) {
        alert("Please, fill in all the fields to add a new product.")
    }
    //console.log(input1.value)
}