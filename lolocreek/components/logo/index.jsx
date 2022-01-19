import cx from 'classnames'

// styles
import StyleCSS from './style.module.css'

export default function Index() {
    return (
        <div className={cx(StyleCSS.logo, 'text-center text-2xl')}>
            Logo
        </div>
    )
}
