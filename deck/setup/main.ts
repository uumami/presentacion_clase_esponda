export default () => {
  if (typeof window === 'undefined')
    return

  try {
    window.localStorage.removeItem('slidev-show-editor')
  }
  catch {
    // ignore
  }

  // Swallow the 'g' key so the Goto dialog never opens.
  const block = (e: KeyboardEvent) => {
    const target = e.target as HTMLElement | null
    const tag = target?.tagName?.toLowerCase()
    if (tag === 'input' || tag === 'textarea' || target?.isContentEditable)
      return
    if (e.key === 'g' || e.key === 'G' || e.key === 'e' || e.key === 'E') {
      e.stopImmediatePropagation()
      e.stopPropagation()
      e.preventDefault()
    }
  }
  window.addEventListener('keydown', block, { capture: true })

  // Fix absolute /img/... refs when deployed under a sub-path (GitHub Pages).
  // Vite's BASE_URL is injected at build time.
  const BASE = (import.meta as any).env?.BASE_URL || '/'
  if (BASE && BASE !== '/') {
    const trimmed = BASE.replace(/\/$/, '')
    const rewrite = (el: Element) => {
      if (el.tagName === 'IMG') {
        const src = el.getAttribute('src')
        if (src && src.startsWith('/') && !src.startsWith('//') && !src.startsWith(trimmed + '/'))
          el.setAttribute('src', trimmed + src)
      }
    }
    const walk = (root: Element | Document) => {
      if ((root as Element).tagName === 'IMG')
        rewrite(root as Element)
      root.querySelectorAll?.('img').forEach(rewrite)
    }
    walk(document)
    const observer = new MutationObserver((mutations) => {
      for (const m of mutations) {
        m.addedNodes.forEach((node) => {
          if (node.nodeType === 1) walk(node as Element)
        })
        if (m.type === 'attributes' && m.target.nodeType === 1) {
          rewrite(m.target as Element)
        }
      }
    })
    observer.observe(document.documentElement, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['src'],
    })
  }
}
