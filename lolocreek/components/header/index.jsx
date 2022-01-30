import { useState } from 'react'
import cx from 'classnames'
import Link from 'next/link'
import Image from 'next/image';

// style
import StyleCSS from './style.module.css'

// components
import Button from 'components/button'
import SideNav from 'components/sideNav';

// images
import LogoImg from 'images/logoWhite.png';


export default function Index(props) {
    const {page} = props

    const style = (loc) => {
        if (page == loc){
            return 'underline'
        }
    }

    return (
        <div id='navbar__wrapper'>
            <div className='md:hidden flex justify-between items-center mr-3'>
                <SideNav />
                <Button 
                text="Contact Us"
                action={{
                    url:'/contact_us'
                }}
                />
            </div>
            <div className={cx('hidden md:grid grid-cols-2 mx-3', StyleCSS.nav)} id='navbar__normal'>
                <div>
                    <div className={cx(StyleCSS.logo, 'md:w-36 lg:w-44')}>
                        <Image
                        src={LogoImg}
                        alt='Logo'
                        />
                    </div>
                </div>
                <div>
                    <ul className='flex gap-3 justify-end place-items-center'>
                        <li className={style('home')}><Link href="/">Home</Link></li>
                        <li className={style('about_us')}><Link href="/about_us">About Us</Link></li>
                        <li className={style('services')}><Link href="/services">Services</Link></li>
                        <li className='hidden md:inline-block'>
                            <Button
                                text="Contact Us"
                                action={{
                                    url: '/contact_us'
                                }}
                            />
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}
