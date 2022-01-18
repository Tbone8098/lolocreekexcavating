import cx from 'classnames'

// style
import StyleCSS from './style.module.css'

// components
import Header from 'components/header'
import Logo from 'components/logo'
import Button from 'components/button'

export default function Index() {

    const infoBlock = () => {
        return (
            <div className={cx(StyleCSS.infoBox, 'flex flex-col gap-3')}>
                <h1 className='text-5xl md:text-8xl'>Lolo Excavating</h1>
                <h2 className='text-2xl'>(123) 456-7890</h2>
                <h2 className='text-md'>brandon@lolocreekexcavating.com</h2>
                <h2 className='text-md'>1234 Somewhere in Montana Lane</h2>
            </div>
        )
    }

    return (
        <div className={cx(StyleCSS.main, 'h-screen grid grid-cols-12')}>
            <div className='col-span-12 h-min pt-4'>
                <Header />
            </div>
            <div className='col-span-8 col-start-3 md:col-start-2 md:col-span-5 grid'>
                <div className='flex flex-col gap-3'>
                    <div className='md:hidden'>
                        <Logo />
                    </div>
                    {infoBlock()}
                    <div className='lg:hidden self-end'>
                        <Button
                            text="Contact Us"
                            action={{
                                url: '/contactus'
                            }}
                            attributes={{
                                'text': 'text-3xl text-white'
                            }}
                        />
                    </div>
                </div>
            </div>
        </div>
    )
}
