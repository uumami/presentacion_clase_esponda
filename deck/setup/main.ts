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
}
