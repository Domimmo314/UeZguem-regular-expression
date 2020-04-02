<?php

function uezguem_check ($input) {
  return preg_match('/\A(u+|w+)e+\s+z+s*(g+|k+)(u+e+|o+)m+\z/i', $input);
}
