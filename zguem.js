function uezguem_check (text) {
  return text.match(/^(u+|w+)e+\s+z+s*(g+|k+)(u+e+|o+)m+$/i) ? 1 : 0;
}
