
const addStyle = (props, base=null) => {

    let string = ""

    for (const attribute in props) {
        base[attribute] = props[attribute]
    }
    
    for (const attribute in base) {
        string += " " + base[attribute]
    }
    return string
}

export default addStyle