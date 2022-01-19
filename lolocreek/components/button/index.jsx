import AddStyle from 'helperFunc/addstyles'
import Link from 'next/link'

export default function Index(props) {
    const {text, attributes, action={}} = props

    const Style = () => {
        let base = {
            'background': 'bg-black',
            'text': 'text-white',
            'padding': 'p-2',
            'rounded': 'rounded',
            'pointer': 'cursor-pointer',
            'display': 'inline-block',
            'margin': 'my-1'
        }
        return AddStyle(attributes, base)
    }

    const Action = () => {
        if (action.hasOwnProperty('url')){
            return <div className={Style()}>
                <Link href={action['url']}>{text}</Link>
            </div>
        }else {
            return <div className={Style()}>
                <button>{text}</button>
            </div>
        }
    }

    return (
        <>
            {Action()}
        </>
    )
}
