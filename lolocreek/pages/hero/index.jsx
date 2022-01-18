import cx from 'classnames'

// style
import StyleCSS from './style.module.css'

// components
import Header from 'components/header'

export default function Index() {
    return (
        <div className={cx(StyleCSS.main)}>
            <div className='pt-6'>
                <Header />
            </div>
        </div>
    )
}
