import cx from 'classnames'
import Link from 'next/link'

// style
import StyleCSS from './style.module.css'

// components
import Button from 'components/button'


export default function Index() {
    return (
        <div id='navbar__wrapper'>
            <div id='navbar__mobile' className='grid md:hidden mx-4'>
                <div className={cx(StyleCSS.hamburger)}><span></span></div>
            </div>
            <div className={cx('hidden md:grid grid-cols-2 mx-3', StyleCSS.nav)} id='navbar__normal'>
                <div className='self-center'>
                    logo
                </div>
                <div>
                    <ul className='flex gap-3 justify-end place-items-center'>
                        <li><Link href="/about">About Us</Link></li>
                        <li><Link href="/services">Services</Link></li>
                        <li className='hidden lg:inline-block'>
                            <Button 
                            text="Contact Us"
                            action={{
                                url: '/contactus'
                            }}
                            />
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}
