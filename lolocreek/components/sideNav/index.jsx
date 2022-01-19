import { useState } from 'react'
import Link from 'next/link'
import cx from 'classnames'
// import {Toggle} from './logic'

// style
import StyleCSS from './style.module.css'
import MainCSS from 'styles/main.module.css'

export default function Index() {
    return (
        <div className={StyleCSS.sidenav__wrapper}>
            <div className={StyleCSS.sidenav__container}>
                <div className={StyleCSS.sidenav__menu}>
                    <ul className={cx(MainCSS.ul__menu__col)}>
                        <li className='text-xl'><Link href='/about'>About Us</Link></li>
                        <li className='text-xl'><Link href='/services'>Services</Link></li>
                    </ul>
                </div>
            </div>
        </div>
    )
}
