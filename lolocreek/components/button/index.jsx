import AddStyle from 'helperFunc/addstyles'
import Link from 'next/link'

export default function Index(props) {
    const {text, attributes, action=null} = props

    const Style = () => {
        let base = {
            'background': 'bg-black',
            'text': 'text-white',
            'padding': 'p-2',
            'rounded': 'rounded',
            'pointer': 'cursor-pointer',
        }
        return AddStyle(attributes, base)
    }

    const Action = () => {
        if (action['url']){
            return <div className={Style()}>
                <Link href={action['url']}>{text}</Link>
            </div>
        }
    }

    return (
        <div>
            {Action()}
        </div>
    )
}
