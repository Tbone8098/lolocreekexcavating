import cx from 'classnames'
import Link from 'next/link'

// style
import StyleCSS from './style.module.css'

// components
import ContactBtn from 'components/contactBtn'


export default function Index() {
    return (
        <div className={cx(StyleCSS.nav, 'grid grid-cols-2')}>
            <div>
                <p>logo</p>
            </div>
            <div className='flex'>
                <ul className='flex gap-3'>
                    <li><Link href="/about">About Us</Link></li>
                    <li><Link href="/services">Services</Link></li>
                    <li><ContactBtn 
                    text="Contact Us"
                    action="modal"
                    /></li>
                </ul>
            </div>
        </div>
    )
}
