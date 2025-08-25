import { Tree } from '@nx/devkit';
import { libraryGenerator } from '@nx/js';
import * as uxGenerator from '@nxlv/python/src/generators/uv-project/generator';
import { CreateLibGeneratorSchema } from './schema';

export async function createLibGenerator(
  tree: Tree,
  {name, ...options}: CreateLibGeneratorSchema
) {
  const projectRoot = `libs/${options.domain}`;
  const dir = name ? `${projectRoot}/${name}/${options.type}` : `${projectRoot}/${options.type}`
  const divider = options.type === 'server' ? '_' : '-';
  const projectName = name ? `${options.domain}${divider}${name}${divider}` : `${options.domain}${divider}${options.type}`;
  if (options.type === 'server') {
    return genServer(tree, projectName, dir, options.domain);
  }
  return genUi(tree, projectName, dir, options.domain);
}

function genServer(tree: Tree, name: string, directory: string, domain: string) {
  return uxGenerator.default(tree, {
    name,
    directory,
    srcDir: true,
    tags: `type:server,scope:${domain}`,
    publishable: false,
    projectType: 'library',
    unitTestRunner: 'pytest',
    buildSystem: 'uv',
    linter: 'ruff',
    pyenvPythonVersion: '3.13.7',
    projectNameAndRootFormat: 'as-provided',
    moduleName: '',
    buildLockedVersions: true,
    buildBundleLocalDependencies: true,
    rootPyprojectDependencyGroup: '',
    pyprojectPythonDependency: '',
    codeCoverage: true,
    codeCoverageHtmlReport: true,
    codeCoverageXmlReport: false,
    unitTestHtmlReport: true,
    unitTestJUnitReport: false
  });
}

function genUi(tree: Tree, name: string, directory: string, domain: string) {
  return libraryGenerator(tree, {
    name,
    directory,
    config: 'project',
    bundler: 'vite',
    buildable: true,
    compiler: 'swc',
    js: false,
    tags: `type:ui,scope:${domain}`,
    publishable: false,
    strict: true,
    testEnvironment: 'jsdom',
    unitTestRunner: 'vitest',
    useProjectJson: true,
  })
}

export default createLibGenerator;
