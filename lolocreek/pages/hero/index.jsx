import cx from 'classnames'

// style
import StyleCSS from './style.module.css'

// components
import { Header, Logo, Button, Footer } from 'components';
import { data } from 'datafiles/companyData';

// image
import LoloLogo from 'images/logoWhite.png';

export default function Index() {

    const infoBlock = () => {
        return (
            <div>
                <div className={cx(StyleCSS.infoBox, 'flex flex-col gap-3')}>
                    <h1 className='hidden md:inline-block text-5xl font-libre font-bold'>{data.title}</h1>
                    <a href={'tel:' + data.phoneNum.cellSimplified}><p className={cx('text-2xl font-cinzel md:text-4xl border-2 rounded-lg shadow-lg md:rounded-none md:shadow-none md:border-none md:hover:text-blue-500')}> {data.phoneNum.cell}</p></a>
                    <a href={'mailto:' + data.email}><p className='text-md font-bree md:text-lg border-2 rounded-lg shadow-lg md:rounded-none md:shadow-none md:border-none md:hover:text-blue-500'>{data.email}</p></a>
                    <p className='text-sm font-bree md:text-lg'>{data.address}</p>
                </div>
            </div>
        )
    }

    return (
        <div className={cx(StyleCSS.main, 'flex flex-col h-screen')}>
            <div className={cx('grid grid-cols-12')}>
                <div className='col-span-12 md:my-5'>
                    <Header page='home' />
                </div>
            </div>
            <div className='mt-auto grid grid-cols-12'>
                <div className='col-span-10 col-start-2 md:col-span-6 md:col-start-2'>
                    <div className='md:flex md:flex-col'>
                        <div className='mb-3 md:hidden'>
                            <Logo
                                img={LoloLogo}
                            />
                        </div>
                        <div className='mb-3 md:col-span-7 md:row-start-1'>
                            {infoBlock()}
                        </div>
                        <div className='md:col-span-3 md:row-start-2 self-end'>
                            <Button
                                text="Contact Us"
                                attributes={{
                                    'text': 'text-3xl md:text-5xl text-lolo-green',
                                    'border': 'border border-2'
                                }}
                                action={{
                                    url: '/contact_us'
                                }}
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div className='mt-auto'>
                <Footer />
            </div>
        </div>
    )
}
