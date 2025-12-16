export default function hasValuesFromArray(array, set) {
  const b_array = new Set(array);
  const b_set = new Set(set);
  for (const elem of b_set) {
    if (!b_array.has(elem)) {
      return false;
    }
  }
  return true;
}