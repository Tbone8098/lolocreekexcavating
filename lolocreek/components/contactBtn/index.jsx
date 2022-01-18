import AddStyle from 'helperFunc/addstyles'

export default function Index(props) {
    const {text, attributes, action=null} = props

    const Style = () => {
        let base = {
            'background': 'bg-black',
            'text': 'text-white',
            'padding': 'p-2',
            'rounded': 'rounded',
            'pointer': 'cursor-pointer'
        }
        return AddStyle(attributes, base)
    }

    const Action = () => {
        console.log(action);
    }

    return (
        <div>
            <span className={Style()} onClick={() => Action()}>{text}</span>
        </div>
    )
}
