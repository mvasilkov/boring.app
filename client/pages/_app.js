import React from 'react'

import 'antd/dist/reset.css'
import '../stylesheets/app.css'

export default function Application({ Component, pageProps }) {
  return <Component {...pageProps} />
}
