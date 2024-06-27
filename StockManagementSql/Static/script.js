function goodString(name, price, quantity){

    // This function matches any empty string.
    return /^\s+$|^$/gi.test(name) || /^\s+$|^$/gi.test(price) || /^\s+$|^$/gi.test(quantity);
}

function checkInputAdd() {

    // This function validates user's input. 
    let input1 = document.getElementById("name_add").value;
    let input2 = document.getElementById("price_add").value;
    let input3 = document.getElementById("quantity_add").value;
    let check = goodString(input1, input2, input3);
    if (check == true ) {
        alert("Please, fill in all the fields to add a new product.")
        return false;
    } else {
        return document.getElementById("form_add").submit();
    }
}

function checkInputUpdate() {
    
    // This function validates user's input.
    let input1 = document.getElementById("name_update").value;
    let input2 = document.getElementById("price_update").value;
    let input3 = document.getElementById("quantity_update").value;
    let check = goodString(input1, input2, input3);
    if (check == true ) {
        alert("Please, fill in all the fields to update a product.")
        return false;
    } else {
        return document.getElementById("form_update").submit();
    }
}

function checkInputDelete() {

    // This function validates user's input.
    let input1 = document.getElementById("product_delete").value;
    let check = /^\s+$|^$/gi.test(input1);
    if (check == true ) {
        alert("Please, fill in the field to delete a product.")
        return false;
    } else {
        return document.getElementById("form_delete").submit();
    }
}

function hideItem(){

    // This function hides the items shown in the application.
    let items = document.getElementById("hide");
    items.textContent = ""
}