export default function hasValuesFromArray(array, set) {
  return (new Set(set).isSubsetOf(array))
}